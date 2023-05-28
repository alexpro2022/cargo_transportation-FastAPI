from geopy.distance import geodesic
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import settings
from app.models import Car, Cargo
from .car import car_crud
from .location import location_crud


async def get_distance(session: AsyncSession, cargo: Cargo, car: Car) -> int:
    coord = []
    for item in (cargo, car):
        location = await location_crud.get_or_404(
            session, item.current_location)
        coord.append((location.lat, location.lng))
    return geodesic(*coord).miles


async def get_cars_amount(session: AsyncSession, cargo: Cargo) -> int:
    counter: int = 0
    for car in await car_crud.get_all(session):
        if car.weight >= cargo.weight:
            distance = await get_distance(session, cargo, car)
            if distance <= settings.MAX_RADIUS:
                counter += 1
    return counter


async def get_car_numbers(
        session: AsyncSession, cargo: Cargo) -> list[tuple[str, int]]:
    result = []
    for car in await car_crud.get_all(session):
        if car.weight >= cargo.weight:
            distance = await get_distance(session, cargo, car)
            result.append((car.number, distance))
    return result
