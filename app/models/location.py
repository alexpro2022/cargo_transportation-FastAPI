from sqlalchemy import Column, String

from app.core.db import Base


class Location(Base):
    zip = Column(String(100), unique=True, nullable=False)
    state = Column(String(256), nullable=False)
    city = Column(String(256), nullable=False)
    lat = Column(String(100), nullable=False)
    lng = Column(String(100), nullable=False)

    def __repr__(self):
        return (
            f'Индекс: {self.zip},\n'
            f'Штат: {self.state},\n'
            f'Город: {self.city},\n'
            f'Широта: {self.lat},\n'
            f'Долгота: {self.lng}.\n\n'
        )
