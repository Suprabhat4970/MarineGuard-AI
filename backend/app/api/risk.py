from app.services.port_service import ports
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
    valid_ports = [port.name.lower() for port in ports]

    if request.start_port.lower() not in valid_ports:
        return {
            "error": "Start port not found"
        }

    if request.destination_port.lower() not in valid_ports:
        return {
            "error": "Destination port not found"
        }
    
    result = calculate_route_risk(
        request.wind_speed,
        request.wave_height,
        request.visibility,
        request.weather_condition
    )

    return {
        "start_port": request.start_port,
        "destination_port": request.destination_port,
        **result
    }