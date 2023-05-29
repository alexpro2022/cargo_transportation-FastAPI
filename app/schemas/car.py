from pydantic import Field

from app.core import settings
from . import mixins
from .location import LocationResponse


class CarUpdate(mixins.CurrentLocationZIP):
    pass


class CarResponse(
    mixins.DB,
    mixins.Weight,
):
    car_location: LocationResponse
    number: str = Field(
        min_length=settings.CAR_NUMBER_LENGTH,
        max_length=settings.CAR_NUMBER_LENGTH,
    )
