from app.schemas.mixins import DBMixin, ZipMixin


class CarResponse(DBMixin):
    pass


class CarUpdate(ZipMixin):
    pass
