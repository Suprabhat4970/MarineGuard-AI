from pydantic import BaseModel


class Vessel(BaseModel):
    name: str
    vessel_type: str
    length: float
    width: float
    draft: float
    latitude: float
    longitude: float