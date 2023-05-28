from pydantic import Field
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import settings
from app.models import Car
from . import mixins
from .utils import include_nested_location
from .location import LocationResponse


class CarUpdate(mixins.CurrentLocationZIP):
    pass


class CarResponse(
    mixins.DB,
    mixins.Weight,
):
    current_location: LocationResponse
    number: str = Field(
        min_length=settings.CAR_NUMBER_LENGTH,
        max_length=settings.CAR_NUMBER_LENGTH,
    )

    @classmethod
    async def to_representation(self, session: AsyncSession, car: Car):
        return await include_nested_location(
            session, car, settings.CURRENT_LOCATION)
