from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class CommonFieldsMixin:
    current_location = Column(Integer, ForeignKey('location.id'))
    weight = Column(Integer, nullable=False)  # carrying_capacity for the cars
