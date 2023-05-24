from fastapi import APIRouter, Depends

from app.core.db import AsyncSession, get_async_session
from app.crud.location import location_crud
from app.schemas.location import Location

router = APIRouter(prefix='/location', tags=['Locations'])


@router.get(
    '/{location_id}',
    response_model=Location,
    response_model_exclude_none=True,
    summary='Возвращает список всех локаций.',
    description='Возвращает список всех локаций.',
)
async def get_location(
    location_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    return await location_crud.get_or_404(session, location_id)
