# from http import HTTPStatus
# from fastapi import HTTPException
# from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.location import location_crud
from app.models.car import Car as model_Car
from app.schemas.car import CarResponse

from app.crud.base import CRUDBase


class CarCRUD(CRUDBase[model_Car, CarResponse, CarResponse]):

    def is_update_allowed(self, obj: model_Car, payload: dict) -> None:
        pass

    async def update_func(self, session, obj, update_data):
        loc = await location_crud.get_by_attr(
            session, 'zip', update_data['zip'])
        obj.current_location = loc.id
        return obj


car_crud = CarCRUD(model_Car)
