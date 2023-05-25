from fastapi import APIRouter, Depends

from app.core.db import AsyncSession, get_async_session
from app.crud.cargo import cargo_crud
from app.schemas.cargo import CargoResponse, CargoUpdate

router = APIRouter(prefix='/cargo', tags=['Cargos'])


@router.get(
    '/',
    response_model=list[CargoResponse],
    response_model_exclude_none=True,
    summary='Возвращает список всех машин.',
    description='Возвращает список всех машин.',
)
async def get_all_cars(
    session: AsyncSession = Depends(get_async_session),
):
    return await cargo_crud.get_all(session)


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
