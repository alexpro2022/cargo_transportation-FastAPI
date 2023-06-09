from typing import Annotated

from fastapi import APIRouter, Depends, Query, encoders

from app.core.db import AsyncSession, get_async_session
from app.crud.cargo import cargo_crud
from app.crud.utils import get_car_numbers, get_cars_amount
from app.schemas.cargo import (CargoCreate, CargoDeleteResponse, CargoResponse,
                               CargoUpdate, GetCargoResponse,
                               GetCargosResponse)

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
    return await cargo_crud.create(session, payload)


@router.put(
    '/{cargo_id}/',
    response_model=CargoResponse,
    summary='Редактирование груза по ID.',
    description='Редактирование груза по ID (вес, описание)',
)
async def update_cargo(
    cargo_id: int,
    payload: CargoUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    return await cargo_crud.update(
        session, cargo_id, payload, perform_update=False)


@router.delete(
    '/{cargo_id}/',
    response_model=CargoDeleteResponse,
    summary='Удаление груза по ID.',
    description='Удаление груза по ID.',
)
async def delete_cargo(
    cargo_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    return await cargo_crud.delete(session, cargo_id)


@router.get(
    '/',
    response_model=list[GetCargosResponse],
    summary='Получение списка грузов.',
    description=(
        'Получение списка грузов с фильтрацией по максимальному весу груза, '
        'задаваемому query-параметром `max_weight`. Список состоит из полей '
        'локаций pick-up / delivery и поля количества ближайших машин '
        '(с подходящей грузоподъемностью) до груза (расстояние до груза '
        'не более кол-ва миль, задаваемых query-параметром `max_distance`)'
    )
)
async def get_all_cargos(
    max_weight: Annotated[int, Query(ge=1, le=1000, example=500)] = 1000,
    max_distance: Annotated[int, Query(ge=1, example=500)] = 450,
    session: AsyncSession = Depends(get_async_session),
):
    return [
        GetCargosResponse(
            **encoders.jsonable_encoder(cargo),
            nearest_cars_amount=await get_cars_amount(
                session, cargo, max_distance))
        for cargo in await cargo_crud.get_all(session)
        if cargo.weight <= max_weight]


@router.get(
    '/{cargo_id}/',
    response_model=GetCargoResponse,
    summary='Получение информации о конкретном грузе по ID.',
    description=(
        'Получение информации о конкретном грузе по ID '
        '(локации pick-up, delivery, вес, описание, список '
        'номеров ВСЕХ (с подходящей грузоподъемностью) машин '
        'с расстоянием до выбранного груза).'),
)
async def get_cargo(
    cargo_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    cargo = await cargo_crud.get_or_404(session, cargo_id)
    return GetCargoResponse(
        **encoders.jsonable_encoder(cargo),
        car_numbers=await get_car_numbers(session, cargo),
    )
