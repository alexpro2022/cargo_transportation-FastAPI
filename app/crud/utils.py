from geopy.distance import geodesic
from sqlalchemy.ext.asyncio import AsyncSession

# from app.core import settings
from app.models import Car, Cargo

from .car import car_crud


# async def get_distance(session: AsyncSession, cargo: Cargo, car: Car) -> int:
async def get_distance(cargo: Cargo, car: Car) -> int:
    return int(geodesic(
        (cargo.pick_up.lat, cargo.pick_up.lng),
        (car.car_location.lat, car.car_location.lng),
    ).miles)


async def get_cars_amount(
        session: AsyncSession, cargo: Cargo, max_distance: int) -> int:
    counter: int = 0
    for car in await car_crud.get_all(session):
        if car.weight >= cargo.weight:
            distance = await get_distance(cargo, car)
            if distance <= max_distance:
                counter += 1
    return counter


async def get_car_numbers(
        session: AsyncSession, cargo: Cargo) -> list[tuple[str, int]]:
    result = []
    for car in await car_crud.get_all(session):
        if car.weight >= cargo.weight:
            distance = await get_distance(cargo, car)
            result.append((car.number, distance))
    return result
