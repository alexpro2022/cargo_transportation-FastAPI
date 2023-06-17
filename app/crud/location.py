from sqlalchemy.ext.asyncio import AsyncSession

from app.core import settings
from app.crud.base import CRUDBase
from app.models.location import Location


class LocationCRUD(CRUDBase[Location, None, None]):
    NOT_FOUND = 'Введен неверный zip-код - проверьте параметры запроса.'

    async def get_location_by_zip(
        self, session: AsyncSession, zip: str
    ) -> Location:
        return await self.get_by_attr(
            session, settings.ZIP, zip, exception=True)


location_crud = LocationCRUD(Location)
