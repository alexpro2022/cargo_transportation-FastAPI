from sqlalchemy.ext.asyncio import AsyncSession

from app.core import settings
from app.crud.base import CRUDBase
from app.crud.location import location_crud
from app.models import Cargo
from app.schemas.cargo import CargoCreate, CargoUpdate


class CargoCRUD(CRUDBase[Cargo, CargoCreate, CargoUpdate]):
    NOT_FOUND = 'Груз не найден, проверьте ID или параметры запроса.'

    async def is_update_allowed(self, obj: Cargo, payload: dict) -> None:
        pass

    async def is_delete_allowed(self, obj: Cargo) -> None:
        pass

    async def perform_create(self, session: AsyncSession, create_data: dict):
        for zip_key, attr_name in (
            (settings.CURRENT_ZIP, settings.CURRENT_LOCATION),
            (settings.DELIVERY_ZIP, settings.DELIVERY_LOCATION),
        ):
            zip = create_data.pop(zip_key)
            loc = await location_crud.get_location_by_zip(session, zip)
            create_data[attr_name] = loc.id


cargo_crud = CargoCRUD(Cargo)
