from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class CommonFieldsMixin:
    item_id = Column(String(5), unique=True, nullable=False, index=True)
    current_location = Column(Integer, ForeignKey('location.id'))
    weight = Column(Integer, nullable=False)  # carrying_capacity for the cars
