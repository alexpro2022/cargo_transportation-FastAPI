from app.schemas import mixins


class CargoResponse(
    mixins.DB,
    mixins.Weight,
    mixins.Description,
    mixins.CurrentLocationFK,
    mixins.DeliveryLocationFK,
):
    pass


class CargoCreate(
    mixins.Weight,
    mixins.Description,
    mixins.CurrentLocationZIP,
    mixins.DeliveryLocationZIP,
):
    pass


class CargoUpdate(
    mixins.Weight,
    mixins.Description,
):
    pass


class CargoResponseGetCargo(CargoResponse):
    pass
    # car_numbers: list


class CargoResponseGetCargos(
    mixins.DB,
    mixins.CurrentLocationFK,
    mixins.DeliveryLocationFK,
):
    pass
    # nearest_cars_amount: int
