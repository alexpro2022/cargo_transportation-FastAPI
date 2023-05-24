from sqlalchemy import Column, ForeignKey, Integer, Text

from app.core.db import Base
from app.models.mixins import CommonFieldsMixin


class Cargo(CommonFieldsMixin, Base):
    description = Column(Text, nullable=False)
    delivery_location = Column(Integer, ForeignKey('location.id'))
    # item_id = Column(String(256), unique=True, nullable=False)
    # weight = Column(Integer, nullable=False)
    # current_location = Column(Integer, ForeignKey('location.id'))

    def __repr__(self):
        return (
            f'Идентификатор груза: {self.item_id},\n'
            f'Описание груза: {self.description},\n'
            f'Вес груза: {self.weight},\n'
            f'Откуда: {self.current_location},\n'
            f'Куда: {self.delivery_location},\n\n'
        )
