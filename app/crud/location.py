from app.models.location import Location as model_Location
from app.schemas.location import LocationResponse as schema_Location

from app.crud.base import CRUDBase


class LocationCRUD(CRUDBase[model_Location, schema_Location, schema_Location]):
    OBJECT_ALREADY_EXISTS = 'Локация с таким zip-кодом уже существует!'

    def is_delete_allowed(self, obj: model_Location) -> None:
        pass

    def is_update_allowed(self, obj: model_Location, payload: dict) -> None:
        pass

    def has_permission(self, obj: model_Location) -> None:
        pass


location_crud = LocationCRUD(model_Location)
