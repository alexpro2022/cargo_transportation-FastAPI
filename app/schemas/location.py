from pydantic import Field

from app.core.config import settings
from app.schemas import mixins


class LocationResponse(mixins.DB):
    zip: str = Field(
        min_length=settings.ZIP_CODE_LENGTH,
        max_length=settings.ZIP_CODE_LENGTH)
    state_name: str = Field(max_length=settings.STATE_NAME_LENGTH)
    city: str = Field(max_length=settings.CITY_NAME_LENGTH)
    lat: str = Field(max_length=settings.COORDINATES_LENGTH)
    lng: str = Field(max_length=settings.COORDINATES_LENGTH)
