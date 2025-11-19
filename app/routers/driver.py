```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.auth import get_current_user, get_db
from app.models.driver import Driver
from app.schemas.driver_schema import DriverAssign

router = APIRouter()

@router.post("/assign")
def assign_driver(data: DriverAssign, user=Depends(get_current_user), db: Session = Depends(get_db)):
    if user["role"] != "admin":
        raise HTTPException(403, "Only admins can assign drivers")

    driver = db.query(Driver).filter(Driver.user_id == data.user_id).first()
    if not driver:
        driver = Driver(user_id=data.user_id)

    driver.bus_id = data.bus_id
    db.add(driver)
    db.commit()
    return {"message": "Driver assigned successfully"}
```
