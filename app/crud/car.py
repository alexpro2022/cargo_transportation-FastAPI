from sqlalchemy.ext.asyncio import AsyncSession

from app.core import settings
from app.crud.base import CRUDBase
from app.crud.location import location_crud
from app.models import Car


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


car_crud = CarCRUD(Car)
