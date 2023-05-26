from fastapi import APIRouter, Depends

from app.core.db import AsyncSession, get_async_session
from app.crud.location import location_crud
from app.schemas.location import LocationResponse

router = APIRouter(prefix='/location', tags=['Locations'])


@router.get(
    '/{location_id}',
    response_model=LocationResponse,
    summary='Возвращает локацию по ID.',
    description='Возвращает локацию по ID. Данного эндпоинта нет в ТЗ.',
)
async def get_location(
    location_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    return await location_crud.get_or_404(session, location_id)
