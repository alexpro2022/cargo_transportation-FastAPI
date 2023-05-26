from app.schemas import mixins
# from app.schemas.location import LocationResponse


class CarResponse(
    mixins.DB,
    mixins.CarNumber,
    mixins.CurrentLocationFK,
    mixins.Weight,
):
    pass


class CarUpdate(mixins.CurrentLocationZIP):
    pass
