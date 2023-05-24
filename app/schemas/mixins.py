from pydantic import BaseModel, Field


class SchemasMixin(BaseModel):
    id: int
    item_id: str = Field(max_length=5)
    current_location: int
    weight: int = Field(gt=0)

    class Config:
        orm_mode = True
