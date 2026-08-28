from fastapi import FastAPI
from app.api.ports import router as ports_router
from app.api.vessels import router as vessels_router
from app.api.routes import router as routes_router
from app.api.weather import router as weather_router
from app.api.risk import router as risk_router

app = FastAPI(
    title="MarineGuard AI",
    description="AI-powered marine traffic, port and route intelligence system",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "MarineGuard AI API is running",
        "status": "online"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(ports_router)
app.include_router(vessels_router)
app.include_router(routes_router)
app.include_router(weather_router)
app.include_router(risk_router)