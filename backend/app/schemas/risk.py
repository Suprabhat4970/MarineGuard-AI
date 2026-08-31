from pydantic import BaseModel


class RouteRiskRequest(BaseModel):
    wind_speed: float
    wave_height: float
    visibility: float
    weather_condition: str
    start_port: str
    destination_port: str