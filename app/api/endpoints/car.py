from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import get_async_session
from app.crud.car import car_crud
from app.schemas.car import CarResponse, CarUpdate

router = APIRouter(prefix='/car', tags=['Cars'])


@router.get(
    '/',
    response_model=list[CarResponse],
    summary='Возвращает список всех машин.',
    description='Возвращает список всех машин. Данного эндпоинта нет в ТЗ.',
)
async def get_all_cars(session: AsyncSession = Depends(get_async_session)):
    cars = await car_crud.get_all(session)
    return [await CarResponse.to_representation(session, car) for car in cars]


@router.put(
    '/{car_id}/',
    response_model=CarResponse,
    summary='Редактирование машины по ID.',
    description=(
        'Редактирование машины по ID '
        '(локация (определяется по введенному zip-коду))'),
)
async def update_car(
    car_id: int,
    payload: CarUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    car = await car_crud.update(session, car_id, payload)
    return await CarResponse.to_representation(session, car)
