from pydantic import BaseModel, Field

from app.core import settings


class DB(BaseModel):
    id: int

    class Config:
        orm_mode = True


class Weight(BaseModel):
    weight: int = Field(ge=1, le=1000)


class CurrentLocationZIP(BaseModel):
    current_zip: str = Field(
        min_length=settings.ZIP_CODE_LENGTH,
        max_length=settings.ZIP_CODE_LENGTH,
    )
