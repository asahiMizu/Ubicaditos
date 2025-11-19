from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importación ÚNICA de todos los routers de los Sprints 1, 2 y 3
from app.routers import auth, bus, route, driver, bus_location, realtime

# Inicialización ÚNICA de la aplicación
app = FastAPI(title="UbicadITOs API")

# Middleware CORS (Necesario para la comunicación entre el frontend y el backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite cualquier origen (debe ser limitado en producción)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Registro ÚNICO de todos los routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(bus.router, prefix="/bus", tags=["Bus"])
app.include_router(route.router, prefix="/routes", tags=["Routes"])
app.include_router(driver.router, prefix="/driver", tags=["Driver"])

# Routers de Sprint 3 (Location y WebSockets)
app.include_router(bus_location.router, prefix="/location", tags=["Location"])
app.include_router(realtime.router, tags=["WebSockets"]) # Este no tiene prefijo, usa /ws/bus/{id}

@app.get("/")
def root():
    return {"msg": "UbicadITOs API Running"}
