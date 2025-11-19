from fastapi import FastAPI
from app.routers import auth

app = FastAPI(title="UbicadITOs API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def root():
    return {"msg": "API Running"}
