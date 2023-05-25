from pydantic import Field

from app.core.config import settings
from app.schemas.mixins import DBMixin, ZipMixin


class CarResponse(DBMixin):
    number: str = Field(
        min_length=settings.CAR_NUMBER_LENGTH,
        max_length=settings.CAR_NUMBER_LENGTH,
    )


class CarUpdate(ZipMixin):
    pass
