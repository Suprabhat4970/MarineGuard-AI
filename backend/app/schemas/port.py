from pydantic import BaseModel


class Port(BaseModel):
    name: str
    latitude: float
    longitude: float
    max_vessel_length: float
    max_vessel_width: float
    max_draft: float
    total_capacity: int
    available_capacity: int
    ships_in_port: int
    waiting_ships: int
    waiting_cost_per_hour: float
    