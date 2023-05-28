from fastapi import APIRouter, Depends

from app.core.db import AsyncSession, get_async_session
from app.crud.cargo import cargo_crud
from app.schemas.cargo import (
    CargoCreate,
    CargoResponse,
    GetCargoResponse1,
    GetCargoResponse2,
    CargoUpdate,
)

router = APIRouter(prefix='/cargo', tags=['Cargos'])


@router.post(
    '/',
    response_model=CargoResponse,
    summary='Создание нового груза.',
    description=(
        'Создание нового груза (характеристики локаций pick-up, '
        'delivery определяются по введенному zip-коду)'),
)
async def create_cargo(
    payload: CargoCreate,
    session: AsyncSession = Depends(get_async_session),
):
    cargo = await cargo_crud.create(session, payload)
    return await CargoResponse.to_representation(session, cargo)


@router.put(
    '/{cargo_id}/',
    response_model=CargoResponse,
    summary='Редактирование груза по ID.',
    description='Редактирование груза по ID (вес, описание)',
)
async def update_cargo_(
    cargo_id: int,
    payload: CargoUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    cargo = await cargo_crud.update(
        session, cargo_id, payload, perform_update=False)
    return await CargoResponse.to_representation(session, cargo)


@router.delete(
    '/{cargo_id}',
    response_model=CargoResponse,
    summary='Удаление груза по ID.',
    description='Удаление груза по ID.',
)
async def delete_cargo_(
    cargo_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    cargo = await cargo_crud.delete(session, cargo_id)
    return await CargoResponse.to_representation(session, cargo)


# =========================
@router.get(
    '/',
    response_model=list[GetCargoResponse2],
    summary='Получение списка грузов.',
    description=(
        'Получение списка грузов (локации pick-up, delivery, '
        'количество ближайших машин (с подходящей грузоподъемностью) '
        'до груза ( =< 450 миль))'),
)
async def get_all_cargos(
    session: AsyncSession = Depends(get_async_session),
):
    cargos = await cargo_crud.get_all(session)
    return [await GetCargoResponse2.to_representation(session, cargo)
            for cargo in cargos]


@router.get(
    '/{cargo_id}',
    response_model=GetCargoResponse1,
    summary='Получение информации о конкретном грузе по ID.',
    description=(
        'Получение информации о конкретном грузе по ID '
        '(локации pick-up, delivery, вес, описание, список '
        'номеров ВСЕХ (с подходящей грузоподъемностью) машин '
        'с расстоянием до выбранного груза).'),
)
async def get_cargo_(
    cargo_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    cargo = await cargo_crud.get_or_404(session, cargo_id)
    return await GetCargoResponse1.to_representation(session, cargo)
