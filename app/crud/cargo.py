from app.models.cargo import Cargo as model_Cargo
from app.schemas.cargo import CargoResponse as schema_Cargo

from app.crud.base import CRUDBase


class CargoCRUD(CRUDBase[model_Cargo, schema_Cargo, schema_Cargo]):
    OBJECT_ALREADY_EXISTS = 'Груз с таким идентификатором уже существует!'

    def is_delete_allowed(self, obj: model_Cargo) -> None:
        pass

    def is_update_allowed(self, obj: model_Cargo, payload: dict) -> None:
        pass

    def has_permission(self, obj: model_Cargo) -> None:
        pass


cargo_crud = CargoCRUD(model_Cargo)
