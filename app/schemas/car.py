from app.schemas import mixins


class CarResponse(
    mixins.DB,
    mixins.CarNumber,
    mixins.CurrentLocationFK,
    mixins.Weight,
):
    pass


class CarUpdate(mixins.CurrentLocationZIP):
    pass
