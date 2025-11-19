from sqlalchemy import Column, Integer, String, Float 
from app.database import Base

class Bus(Base):
    __tablename__ = "buses"

    id = Column(Integer, primary_key=True, index=True)
    plate_number = Column(String, unique=True, index=True)
    capacity = Column(Integer)
    status = Column(String, default="idle")  # idle | en_route | maintenance
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
