from sqlalchemy import Column, String

from app.core import config, db


class Location(db.Base):
    zip = Column(
        String(config.settings.ZIP_CODE_LENGTH),
        unique=True, nullable=False, index=True)
    state_name = Column(String(256), nullable=False)
    city = Column(String(256), nullable=False)
    lat = Column(String(10), nullable=False)
    lng = Column(String(10), nullable=False)

    def __repr__(self):
        return (
            f'ID локации: {self.id},\n'
            f'Индекс: {self.zip},\n'
            f'Штат: {self.state},\n'
            f'Город: {self.city},\n'
            f'Широта: {self.lat},\n'
            f'Долгота: {self.lng}.\n\n'
        )
