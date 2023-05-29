from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class CommonFieldsMixin:
    weight = Column(Integer, nullable=False)  # carrying_capacity for the cars
