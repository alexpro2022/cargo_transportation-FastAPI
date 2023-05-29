from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core import db, settings
from app.models.mixins import CommonFieldsMixin


class Car(CommonFieldsMixin, db.Base):
    number = Column(
        String(settings.CAR_NUMBER_LENGTH),
        unique=True, nullable=False, index=True)
    current_location = Column(Integer, ForeignKey('location.id'))
    car_location = relationship('Location', lazy='joined')

    def __repr__(self):
        return (
            f'ID машины: {self.id},\n'
            f'Номер машины: {self.number},\n'
            f'Грузоподъемность: {self.weight},\n'
            f'Текущая локация машины: {self.current_location}.\n\n'
        )
