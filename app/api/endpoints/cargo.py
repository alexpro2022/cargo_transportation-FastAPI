from fastapi import APIRouter, Depends

from app.core.db import AsyncSession, get_async_session
from app.crud.cargo import cargo_crud
from app.schemas.cargo import (
    CargoCreate,
    CargoResponse,
    # CargoResponseGetCargo,
    CargoResponseGetCargos,
    # CargoUpdate,
)

router = APIRouter(prefix='/cargo', tags=['Cargos'])


@router.post(
    '/',
    response_model=CargoResponse,
    # response_model_exclude_none=True,
    summary='Создание нового груза.',
    description=(
        'Создание нового груза (характеристики локаций pick-up, '
        'delivery определяются по введенному zip-коду)'),
)
async def create_cargo(
    payload: CargoCreate,
    session: AsyncSession = Depends(get_async_session),
):
    return await cargo_crud.create(session, payload)


@router.get(
    '/',
    response_model=list[CargoResponseGetCargos],
    # response_model_exclude_none=True,
    summary='Возвращает список всех грузов.',
    description=(
        'Получение списка грузов (локации pick-up, delivery, '
        'количество ближайших машин до груза ( =< 450 миль))'),
)
async def get_all_cargos(
    session: AsyncSession = Depends(get_async_session),
):
    return await cargo_crud.get_all(session)


@router.delete(
    '/{cargo_id}',
    response_model=CargoResponse,
    summary='Удаление груза по ID.',
    description='Удаление груза по ID.',
)
async def delete_cargo(
    cargo_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    return await cargo_crud.delete(session, cargo_id)


'''
@router.patch(
    '/{car_id}/',
    response_model=CargoResponse,
    summary='Редактирование локации машины.',
    description='Редактирование локации машины.',
)
async def update_car_location(
    car_id: int,
    payload: CargoUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    return await cargo_crud.update(session, car_id, payload)
'''
