from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.auth import get_current_user, get_db
from app.models.route import Route
from app.schemas.route_schema import RouteCreate, RouteOut

router = APIRouter()

@router.post("/create", response_model=RouteOut)
def create_route(route: RouteCreate, user=Depends(get_current_user), db: Session = Depends(get_db)):
    if user["role"] != "admin":
        raise HTTPException(403, "Only admins can create routes")
    
    new_route = Route(**route.dict())
    db.add(new_route)
    db.commit()
    db.refresh(new_route)
    return new_route

@router.get("/list", response_model=list[RouteOut])
def list_routes(db: Session = Depends(get_db)):
    return db.query(Route).all()
