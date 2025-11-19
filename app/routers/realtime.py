from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from app.utils.auth import get_db
from app.models.bus import Bus

router = APIRouter()

active_connections = {}

async def connect_bus(bus_id: int, websocket: WebSocket):
    await websocket.accept()
    active_connections[bus_id] = websocket

async def broadcast_location(bus_id: int, latitude: float, longitude: float):
    if bus_id in active_connections:
        await active_connections[bus_id].send_json({
            "bus_id": bus_id,
            "latitude": latitude,
            "longitude": longitude
        })

@router.websocket("/ws/bus/{bus_id}")
async def bus_socket(websocket: WebSocket, bus_id: int):
    await connect_bus(bus_id, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            latitude = data["latitude"]
            longitude = data["longitude"]
            await broadcast_location(bus_id, latitude, longitude)
    except WebSocketDisconnect:
        active_connections.pop(bus_id, None)
