from sqlalchemy.ext.asyncio import AsyncSession

from app.core import AsyncSessionLocal, get_random_location, settings
from app.crud.base import CRUDBase
from app.crud.location import location_crud
from app.models import Car
from app.schemas.car import CarUpdateCurrentLocation


class CarCRUD(CRUDBase[Car, None, None]):
    NOT_FOUND = 'Машина не найдена, проверьте ID или параметры запроса.'

    async def is_update_allowed(self, obj: Car, payload: dict) -> None:
        pass

    async def perform_update(
        self, session: AsyncSession, obj: Car, update_data: dict,
    ) -> Car:
        current_location = await location_crud.get_location_by_zip(
            session, update_data[settings.CURRENT_ZIP])
        obj.current_location = current_location.id
        return obj

    async def update_cars_location(self) -> None:
        async with AsyncSessionLocal() as session:
            [await self.update(
                session,
                car.id,
                payload=CarUpdateCurrentLocation(
                    current_location=get_random_location()),
                perform_update=False,
            ) for car in await self.get_all(session)]


car_crud = CarCRUD(Car)
