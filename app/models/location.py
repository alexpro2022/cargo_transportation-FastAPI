from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class Location(Base):
    zip = Column(String(5), unique=True, nullable=False, index=True)
    state_name = Column(String(256), nullable=False)
    city = Column(String(256), nullable=False)
    lat = Column(String(10), nullable=False)
    lng = Column(String(10), nullable=False)
    cars = relationship('Car', cascade='delete')
    # cargos = relationship('Cargo', cascade='delete')

    def __repr__(self):
        return (
            f'Индекс: {self.zip},\n'
            f'Штат: {self.state},\n'
            f'Город: {self.city},\n'
            f'Широта: {self.lat},\n'
            f'Долгота: {self.lng}.\n\n'
        )
