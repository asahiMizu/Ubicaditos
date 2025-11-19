```python
from sqlalchemy import Column, Integer, String
from app.database import Base

class Bus(Base):
    __tablename__ = "buses"

    id = Column(Integer, primary_key=True, index=True)
    plate_number = Column(String, unique=True, index=True)
    capacity = Column(Integer)
    status = Column(String, default="idle")  # idle | en_route | maintenance
```
