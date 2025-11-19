from pydantic import BaseModel

class DriverAssign(BaseModel):
    user_id: int
    bus_id: int
