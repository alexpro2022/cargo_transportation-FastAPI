from pydantic import BaseModel

from app.schemas.mixins import DBMixin


class CargoResponse(DBMixin, BaseModel):
    description = str
    delivery_location = int
