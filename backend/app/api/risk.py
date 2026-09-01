from app.services.port_service import ports
from fastapi import APIRouter
from app.schemas.risk import RouteRiskRequest
from app.services.risk_service import calculate_route_risk
from app.services.weather_service import get_weather

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
    valid_ports = [port.name.lower() for port in ports]

    if request.start_port.lower() not in valid_ports:
        return {
            "error": "Start port not found"
        }

    if request.destination_port.lower() not in valid_ports:
        return {
            "error": "Destination port not found"
        }
    start_port = next(
    port for port in ports
    if port.name.lower() == request.start_port.lower()
)
    weather = get_weather(
    start_port.latitude,
    start_port.longitude
)
    
    result = calculate_route_risk(
    weather["wind_speed"],
    weather["wave_height"],
    weather["visibility"],
    weather["weather_condition"]
)

    return {
        "start_port": request.start_port,
        "destination_port": request.destination_port,
        **result
    }