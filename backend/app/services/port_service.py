from app.schemas.port import Port
from app.schemas.vessel import Vessel


ports = [

    Port(
        name="Port Alpha",
        latitude=20.25,
        longitude=85.80,
        max_vessel_length=300,
        max_vessel_width=50,
        max_draft=14,
        total_capacity=30,
        available_capacity=8,
        ships_in_port=22,
        waiting_ships=7
    ),

    Port(
        name="Port Beta",
        latitude=21.10,
        longitude=86.70,
        max_vessel_length=250,
        max_vessel_width=40,
        max_draft=11,
        total_capacity=20,
        available_capacity=0,
        ships_in_port=20,
        waiting_ships=12
    )
]


def get_all_ports():
    return ports


def check_port_availability(port_name: str, vessel: Vessel):

    for port in ports:

        if port.name.lower() == port_name.lower():

            if vessel.length > port.max_vessel_length:
                return {
                    "port": port.name,
                    "available": False,
                    "reason": "Vessel is too long for this port"
                }

            if vessel.width > port.max_vessel_width:
                return {
                    "port": port.name,
                    "available": False,
                    "reason": "Vessel is too wide for this port"
                }

            if vessel.draft > port.max_draft:
                return {
                    "port": port.name,
                    "available": False,
                    "reason": "Vessel draft is too deep for this port"
                }

            if port.available_capacity <= 0:
                return {
                    "port": port.name,
                    "available": False,
                    "reason": "No available capacity"
                }

            return {
                "port": port.name,
                "available": True,
                "reason": "Port can accept the vessel"
            }

    return {
        "port": port_name,
        "available": False,
        "reason": "Port not found"
    }
def estimate_waiting_time(port_name: str):
    for port in ports:
        if port.name.lower() == port_name.lower():

            average_service_time = 0.5

            waiting_time = port.waiting_ships * average_service_time

            return {
                "port": port.name,
                "waiting_ships": port.waiting_ships,
                "estimated_waiting_time_hours": waiting_time
            }

    return {
        "port": port_name,
        "error": "Port not found"
    }