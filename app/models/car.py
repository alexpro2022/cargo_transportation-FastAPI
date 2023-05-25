from sqlalchemy import Column, String

from app.core import config, db
from app.models.mixins import CommonFieldsMixin


class Car(CommonFieldsMixin, db.Base):
    number = Column(
        String(config.settings.CAR_NUMBER_LENGTH),
        unique=True, nullable=False, index=True)

    def __repr__(self):
        return (
            f'ID машины: {self.id},\n'
            f'Номер машины: {self.number},\n'
            f'Грузоподъемность: {self.weight},\n'
            f'Текущая локация машины: {self.current_location}.\n\n'
        )
