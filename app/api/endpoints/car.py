from fastapi import APIRouter, Depends

from app.core.db import AsyncSession, get_async_session
from app.crud.car import car_crud
from app.schemas.car import CarResponse, CarUpdate

router = APIRouter(prefix='/car', tags=['Cars'])


@router.get(
    '/',
    response_model=list[CarResponse],
    response_model_exclude_none=True,
    summary='Возвращает список всех машин.',
    description='Возвращает список всех машин.',
)
async def get_all_cars(
    session: AsyncSession = Depends(get_async_session),
):
    return await car_crud.get_all(session)


@router.patch(
    '/{car_id}/',
    response_model=CarResponse,
    summary='Редактирование локации машины.',
    description='Редактирование локации машины.',
)
async def update_car_location(
    car_id: int,
    payload: CarUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    return await car_crud.update(session, car_id, payload)
