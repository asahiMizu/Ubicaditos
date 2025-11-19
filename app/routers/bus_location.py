from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.auth import get_current_user, get_db
from app.models.bus import Bus
from app.schemas.location_schema import BusLocationUpdate

router = APIRouter()

@router.post("/update")
def update_location(data: BusLocationUpdate, user=Depends(get_current_user), db: Session = Depends(get_db)):
    bus = db.query(Bus).filter(Bus.id == data.bus_id).first()
    bus.latitude = data.latitude
    bus.longitude = data.longitude
    db.commit()
    return {"message": "Location updated"}
