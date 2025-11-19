from pydantic import BaseModel

class BusCreate(BaseModel):
    plate_number: str
    capacity: int

class BusOut(BaseModel):
    id: int
    plate_number: str
    capacity: int
    status: str
    
    class Config:
        orm_mode = True
