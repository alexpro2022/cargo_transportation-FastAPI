from pydantic import BaseModel

from app.schemas.mixins import SchemasMixin


class CargoResponse(SchemasMixin, BaseModel):
    description = str
    delivery_location = int
