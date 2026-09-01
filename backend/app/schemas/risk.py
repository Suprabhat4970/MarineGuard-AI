from pydantic import BaseModel


class RouteRiskRequest(BaseModel):
    start_port: str
    destination_port: str