from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.auth import get_current_user, get_db
from app.models.bus import Bus
from app.schemas.bus_schema import BusCreate, BusOut

router = APIRouter()

@router.post("/create", response_model=BusOut)
def create_bus(bus: BusCreate, user=Depends(get_current_user), db: Session = Depends(get_db)):
    if user["role"] != "admin":
        raise HTTPException(403, "Only admins can create buses")

    new_bus = Bus(
        plate_number=bus.plate_number,
        capacity=bus.capacity
    )
    db.add(new_bus)
    db.commit()
    db.refresh(new_bus)
    return new_bus

@router.get("/list", response_model=list[BusOut])
def list_buses(db: Session = Depends(get_db)):
    return db.query(Bus).all()
