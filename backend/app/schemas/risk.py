from pydantic import BaseModel


class RouteRiskRequest(BaseModel):
    wind_speed: float
    wave_height: float
    visibility: float
    weather_condition: str