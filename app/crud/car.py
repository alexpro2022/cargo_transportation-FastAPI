# from http import HTTPStatus
# from fastapi import HTTPException
# from sqlalchemy.ext.asyncio import AsyncSession

from app.models.car import Car as model_Car
from app.schemas.car import Car as schema_Car

from app.crud.base import CRUDBase


class CarCRUD(CRUDBase[model_Car, schema_Car, schema_Car]):
    OBJECT_ALREADY_EXISTS = 'Машина с таким идентификатором уже существует!'

    def is_delete_allowed(self, obj: model_Car) -> None:
        pass

    def is_update_allowed(self, obj: model_Car, payload: dict) -> None:
        pass

    def has_permission(self, obj: model_Car) -> None:
        pass


car_crud = CarCRUD(model_Car)
