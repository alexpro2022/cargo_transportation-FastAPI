from fastapi import APIRouter, Depends

router = APIRouter(prefix='/car', tags=['Cars'])


@router.get(
    '/',
    response_model=List[schemas.CharityResponse],
    response_model_exclude_none=True,
    summary='Возвращает список всех проектов.',
    description=(
        f'{settings.ALL_USERS}' +
        'Возвращает список всех проектов.'
    ))
async def get_all_charity_projects(
    session: AsyncSession = Depends(get_async_session),
):
    return await charity_crud.get_all(session)


@router.patch(
    '/{car_id}',
    response_model=
)