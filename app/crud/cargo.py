from app.crud.base import CRUDBase
from app.models.cargo import Cargo
from app.schemas.cargo import CargoCreate, CargoUpdate


class CargoCRUD(CRUDBase[Cargo, CargoCreate, CargoUpdate]):
    OBJECT_ALREADY_EXISTS = 'Груз с таким идентификатором уже существует!'

    async def has_permission(self, obj: Cargo) -> None:
        pass

    async def is_update_allowed(self, obj: Cargo, payload: dict) -> None:
        pass

    async def is_delete_allowed(self, obj: Cargo) -> None:
        pass

    #async def perform_create(self, create_data: dict):
    #    pass


cargo_crud = CargoCRUD(Cargo)
