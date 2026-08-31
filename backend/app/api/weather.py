from fastapi import APIRouter
from app.services.weather_service import get_weather as fetch_weather

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)


@router.get("/")

def get_weather():
    return {
        "message": "Weather service is working"
    }

@router.get("/location")
def weather_by_location(latitude: float, longitude: float):
    return fetch_weather(latitude, longitude)