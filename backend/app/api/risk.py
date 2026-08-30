from fastapi import APIRouter
from app.schemas.risk import RouteRiskRequest
from app.services.risk_service import calculate_route_risk

router = APIRouter(
    prefix="/risk",
    tags=["Risk"]
)


@router.get("/")
def get_risk():
    return {
        "message": "Risk service is working"
    }

@router.post("/calculate")
def calculate_risk(request: RouteRiskRequest):
    return calculate_route_risk(
        request.wind_speed,
        request.wave_height,
        request.visibility,
        request.weather_condition
    )