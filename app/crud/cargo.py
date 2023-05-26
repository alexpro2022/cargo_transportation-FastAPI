from fastapi.encoders import jsonable_encoder
from geopy.distance import geodesic
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.crud.base import CRUDBase
from app.crud.car import car_crud
from app.crud.location import location_crud
from app.models.car import Car
from app.models.cargo import Cargo
from app.schemas.cargo import CargoCreate, CargoUpdate


class CargoCRUD(CRUDBase[Cargo, CargoCreate, CargoUpdate]):
    OBJECT_ALREADY_EXISTS = 'Груз с таким идентификатором уже существует!'
    NOT_FOUND = 'Груз не найден, проверьте ID или параметры запроса.'

    async def is_update_allowed(self, obj: Cargo, payload: dict) -> None:
        pass

    async def is_delete_allowed(self, obj: Cargo) -> None:
        pass

    async def perform_create(self, session: AsyncSession, create_data: dict):
        async def get_location_id_by_zip(zip_key: str, attr_name: str):
            zip = create_data.pop(zip_key)
            location = await location_crud.get_location_by_zip(session, zip)
            create_data[attr_name] = location.id

        await get_location_id_by_zip('current_zip', 'current_location')
        await get_location_id_by_zip('delivery_zip', 'delivery_location')

    async def perform_update(
        self, session: AsyncSession, obj: Cargo, update_data: dict
    ) -> Cargo:
        return await self.perform_update_not_nested(session, obj, update_data)

    async def __get_distance(
        self, session: AsyncSession, cargo: Cargo, car: Car
    ) -> int:
        coord = []
        for item in (cargo, car):
            location = await location_crud.get_or_404(
                session, item.current_location)
            coord.append((location.lat, location.lng))
        return geodesic(*coord).miles

    async def get_cargo_or_404(self, session: AsyncSession, pk: int) -> dict:
        async def get_car_numbers() -> list[tuple[str, int]]:
            result = []
            for car in await car_crud.get_all(session):
                if car.weight >= cargo.weight:
                    distance = await self.__get_distance(session, cargo, car)
                    result.append((car.number, distance))
            return result

        cargo = await self.get_or_404(session, pk)
        d = jsonable_encoder(cargo)
        d['car_numbers'] = await get_car_numbers()
        return d

    async def get_all(self, session: AsyncSession) -> list[dict]:
        async def get_cars_amount():
            counter: int = 0
            for car in await car_crud.get_all(session):
                if car.weight >= cargo.weight:
                    distance = await self.__get_distance(session, cargo, car)
                    if distance <= settings.MAX_RADIUS:
                        counter += 1
            return counter

        cargos = []
        for cargo in await super().get_all(session):
            d = jsonable_encoder(cargo)
            d['nearest_cars_amount'] = await get_cars_amount()
            cargos.append(d)
        return cargos


cargo_crud = CargoCRUD(Cargo)
