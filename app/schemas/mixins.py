from pydantic import BaseModel, Field

from app.core.config import settings


class ZipMixin(BaseModel):
    zip: str = Field(
        min_length=settings.ZIP_CODE_LENGTH,
        max_length=settings.ZIP_CODE_LENGTH,
    )


class WeightMixin(BaseModel):
    weight: int = Field(gt=0)


class DescriptionMixin(BaseModel):
    description: str


class DBMixin(WeightMixin):
    id: int
    current_location: int

    class Config:
        orm_mode = True
