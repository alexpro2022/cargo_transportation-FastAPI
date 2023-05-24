from fastapi import APIRouter, Depends

from app.core.db import AsyncSession, get_async_session
from app.crud.car import car_crud
from app.schemas.car import Car

router = APIRouter(prefix='/car', tags=['Cars'])


@router.get(
    '/',
    response_model=list[Car],
    response_model_exclude_none=True,
    summary='Возвращает список всех машин.',
    description='Возвращает список всех машин.',
)
async def get_all_cars(
    session: AsyncSession = Depends(get_async_session),
):
    return await car_crud.get_all(session)


@router.post(
    '/',
    response_model=Car,
    response_model_exclude_none=True,
    # dependencies=[Depends(current_superuser)],
    summary='Создание благотворительного проекта.',
    # description=('Создаёт благотворительный проект.'
)
async def create_car(
    payload: Car,
    session: AsyncSession = Depends(get_async_session),
):
    new_car = await car_crud.create(session, payload)
    # await session.refresh(new_project)
    return new_car


'''@router.patch(
    '/{project_id}',
    response_model=schemas.CharityResponse,
    dependencies=[Depends(current_superuser)],
    summary='Редактирование проекта.',
    description=(
        f'{settings.SUPER_ONLY}' +
        'Закрытый проект нельзя редактировать. '
        'Нельзя установить требуемую сумму меньше уже вложенной.'
    ))
async def update_charity_project(
    project_id: int,
    payload: schemas.CharityUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    updated = await charity_crud.update(session, project_id, payload)
    await calculate_investments(session, updated)
    await session.refresh(updated)
    return updated'''
