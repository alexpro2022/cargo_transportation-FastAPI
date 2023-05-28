from pydantic import Field
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import settings
from app.crud import utils as crud
from app.models import Cargo
from . import mixins, utils
from .location import LocationResponse


# IN
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


# OUT
class CargoOutBase(mixins.DB):
    current_location: LocationResponse
    delivery_location: LocationResponse

    @classmethod
    async def to_representation(
            self, session: AsyncSession, cargo: Cargo) -> dict:
        cargo = await utils.include_nested_location(
            session, cargo, settings.CURRENT_LOCATION)
        return await utils.include_nested_location(
            session, cargo, settings.DELIVERY_LOCATION)


class CargoResponse(
    CargoInBase,
    CargoOutBase,
):
    pass


class GetCargoResponse1(CargoResponse):
    car_numbers: list[tuple[str, int]]

    @classmethod
    async def to_representation(
            self, session: AsyncSession, cargo: Cargo) -> dict:
        car_numbers = await crud.get_car_numbers(session, cargo)
        cargo = utils.include_nested(
            cargo, ((settings.CAR_NUMBERS, car_numbers),))
        return await super().to_representation(session, cargo)


class GetCargoResponse2(CargoOutBase):
    nearest_cars_amount: int

    @classmethod
    async def to_representation(
            self, session: AsyncSession, cargo: Cargo) -> dict:
        nearest_cars_amount = await crud.get_cars_amount(session, cargo)
        cargo = utils.include_nested(
            cargo, ((settings.NEAREST_CARS_AMOUNT, nearest_cars_amount),))
        return await super().to_representation(session, cargo)
