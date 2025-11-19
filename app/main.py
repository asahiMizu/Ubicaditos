from fastapi import FastAPI
from app.routers import auth

app = FastAPI(title="UbicadITOs API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(bus.router, prefix="/bus", tags=["Bus"])
app.include_router(route.router, prefix="/routes", tags=["Routes"])
app.include_router(driver.router, prefix="/driver", tags=["Driver"])
@app.get("/")
def root():
    return {"msg": "API Running"}
