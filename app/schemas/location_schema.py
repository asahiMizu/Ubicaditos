from pydantic import BaseModel

class BusLocationUpdate(BaseModel):
    bus_id: int
    latitude: float
    longitude: float
