def check_location(location):
    assert isinstance(location, dict)
    assert isinstance(location['id'], int)
    assert isinstance(location['zip'], str)
    assert isinstance(location['city'], str)
    assert isinstance(location['lat'], str)
    assert isinstance(location['lng'], str)
    return 'DONE'


def check_car(car):
    assert isinstance(car, dict)
    assert isinstance(car['id'], int)
    assert isinstance(car['weight'], int)
    assert isinstance(car['number'], str)
    return check_location(car['car_location'])


def check_cars(cars):
    assert isinstance(cars, list)
    assert len(cars) == 20
    assert cars == sorted(cars, key=lambda car: car['id'])
    for car in cars:
        res = check_car(car)
    return res