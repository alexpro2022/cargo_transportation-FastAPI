from pydantic import BaseModel, Field

from app.core import settings
from . import mixins
from .location import LocationResponse


class CargoInBase(
    mixins.Weight,
):
    description: str


class CargoCreate(
    mixins.CurrentLocationZIP,
    CargoInBase,
):
    delivery_zip: str = Field(
        min_length=settings.ZIP_CODE_LENGTH,
        max_length=settings.ZIP_CODE_LENGTH,
    )


class CargoUpdate(CargoInBase):
    pass


class CargoOutBase(mixins.DB):
    pick_up: LocationResponse
    delivery: LocationResponse


class CargoResponse(
    CargoInBase,
    CargoOutBase,
):
    pass


class CargoDeleteResponse(mixins.DB, CargoInBase):
    pass


class GetCargosResponse(BaseModel):
    cargo: CargoOutBase
    nearest_cars_amount: int


class GetCargoResponse(BaseModel):
    cargo: CargoResponse
    car_numbers: list[tuple[str, int]]
