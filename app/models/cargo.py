from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from app.core.db import Base
from app.models.mixins import CommonFieldsMixin


class Cargo(CommonFieldsMixin, Base):
    description = Column(Text, nullable=False)
    current_location = Column(Integer, ForeignKey('location.id'))
    delivery_location = Column(Integer, ForeignKey('location.id'))
    pick_up = relationship(
        'Location', lazy='joined', foreign_keys=[current_location])
    delivery = relationship(
        'Location', lazy='joined', foreign_keys=[delivery_location])

    def __repr__(self):
        return (
            f'ID груза: {self.id},\n'
            f'Описание груза: {self.description},\n'
            f'Вес груза: {self.weight},\n'
            f'Откуда: {self.current_location},\n'
            f'Куда: {self.delivery_location},\n\n'
        )
