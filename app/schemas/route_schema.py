from pydantic import BaseModel

class RouteCreate(BaseModel):
    name: str
    origin: str
    destination: str

class RouteOut(BaseModel):
    id: int
    name: str
    origin: str
    destination: str

    class Config:
        orm_mode = True
