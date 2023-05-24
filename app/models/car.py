from app.core.db import Base
from app.models.mixins import CommonFieldsMixin


class Car(CommonFieldsMixin, Base):
    pass
    # item_id = Column(String(5), unique=True, nullable=False)
    # current_location = Column(Integer, ForeignKey('location.id'))
    # weight = Column(Integer, nullable=False)

    def __repr__(self):
        return (
            f'Идентификатор машины: {self.item_id},\n'
            f'Грузоподъемность: {self.weight},\n'
            f'Текущая локация машины: {self.current_location}.\n\n'
        )
