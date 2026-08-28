from fastapi import APIRouter
from app.schemas.vessel import Vessel
from app.services.port_service import estimate_waiting_time
from app.services.port_service import (
    get_all_ports,
    check_port_availability,
    estimate_waiting_time
)


router = APIRouter(
    prefix="/ports",
    tags=["Ports"]
)


@router.get("/")
def get_ports():
    return get_all_ports()


@router.post("/check-availability/{port_name}")
def check_availability(port_name: str, vessel: Vessel):
    return check_port_availability(port_name, vessel)

@router.get("/waiting-time/{port_name}")
def get_waiting_time(port_name: str):
    return estimate_waiting_time(port_name)