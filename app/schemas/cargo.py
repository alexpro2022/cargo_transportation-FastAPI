from app.schemas.mixins import DBMixin, DescriptionMixin, WeightMixin


class CargoResponse(DBMixin, DescriptionMixin):
    delivery_location: int


class CargoUpdate(DescriptionMixin, WeightMixin):
    pass
