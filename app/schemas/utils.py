from typing import Any

from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.location import location_crud


def include_nested(obj, items: list[tuple[str, Any]]) -> dict:
    d = jsonable_encoder(obj)
    for key, value in items:
        d[key] = jsonable_encoder(value)
    return d


async def include_nested_location(
        session: AsyncSession, obj, attr: str) -> dict:
    if isinstance(obj, dict):
        pk = obj[attr]
    else:
        pk = getattr(obj, attr)
    location = await location_crud.get_or_404(session, pk)
    return include_nested(obj, ((attr, location),))
