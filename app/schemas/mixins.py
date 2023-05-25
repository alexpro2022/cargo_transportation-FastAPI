from pydantic import BaseModel, Field


class DBMixin(BaseModel):
    id: int
    item_id: str = Field(min_length=5, max_length=5)
    current_location: int
    weight: int = Field(gt=0)

    class Config:
        orm_mode = True


class ZipMixin(BaseModel):
    zip: str = Field(min_length=5, max_length=5)
