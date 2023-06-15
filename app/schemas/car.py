from pydantic import BaseModel, Field

from app.core import settings
from . import mixins
from .location import LocationResponse


class CarUpdate(mixins.CurrentLocationZIP):
    pass


class CarUpdateCurrentLocation(BaseModel):
    current_location: int


class CarResponse(
    mixins.DB,
    mixins.Weight,
):
    car_location: LocationResponse
    number: str = Field(
        min_length=settings.CAR_NUMBER_LENGTH,
        max_length=settings.CAR_NUMBER_LENGTH,
    )
