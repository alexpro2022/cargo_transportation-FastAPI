from pydantic import BaseModel, Field

from app.core.config import settings


class CarNumber(BaseModel):
    number: str = Field(
        min_length=settings.CAR_NUMBER_LENGTH,
        max_length=settings.CAR_NUMBER_LENGTH,
    )


class Weight(BaseModel):
    weight: int = Field(ge=1, le=1000)


class Description(BaseModel):
    description: str


class CurrentLocationFK(BaseModel):
    current_location: int


class CurrentLocationZIP(BaseModel):
    current_zip: str = Field(
        min_length=settings.ZIP_CODE_LENGTH,
        max_length=settings.ZIP_CODE_LENGTH,
    )


class DeliveryLocationFK(BaseModel):
    delivery_location: int


class DeliveryLocationZIP(BaseModel):
    delivery_zip: str = Field(
        min_length=settings.ZIP_CODE_LENGTH,
        max_length=settings.ZIP_CODE_LENGTH,
    )


class DB(BaseModel):
    id: int

    class Config:
        orm_mode = True
