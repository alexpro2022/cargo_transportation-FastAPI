from pydantic import Field

from app.schemas.mixins import ZipMixin


class LocationResponse(ZipMixin):
    id: int
    state_name: str = Field(max_length=256)
    city: str = Field(max_length=256)
    lat: str = Field(max_length=100)
    lng: str = Field(max_length=100)

    class Config:
        orm_mode = True
