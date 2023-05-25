from pydantic import BaseModel, Field

from app.schemas.mixins import ZipMixin


class LocationResponse(ZipMixin, BaseModel):
    id: int
    # zip: str = Field(max_length=100)
    state_name: str = Field(max_length=256)
    city: str = Field(max_length=256)
    lat: str = Field(max_length=100)
    lng: str = Field(max_length=100)

    class Config:
        orm_mode = True
