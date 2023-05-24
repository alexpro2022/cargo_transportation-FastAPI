from pydantic import BaseModel, Field


class LocationResponse(BaseModel):
    id: int
    zip: str = Field(max_length=100)
    state: str = Field(max_length=256)
    city: str = Field(max_length=256)
    lat: str = Field(max_length=100)
    lng: str = Field(max_length=100)

    class Config:
        orm_mode = True
