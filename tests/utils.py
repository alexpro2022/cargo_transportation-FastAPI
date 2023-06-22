from .fixtures.data import (get_cargo_get_all_response_example,
                            get_cargo_get_id_response_example,
                            get_cargo_post_response_example,
                            get_cargo_put_response_example)


def empty_list(response_json) -> str:
    assert response_json == []
    return 'DONE'


def __assert(response_json: dict, example: dict) -> str:
    assert isinstance(response_json, dict)
    assert isinstance(example, dict)
    response_json.pop('id')
    assert response_json == example, (f'{response_json}\n{example}\n')
    return 'DONE'


def check_cargo_post_response(response_json: dict) -> str:
    return __assert(response_json, get_cargo_post_response_example())


def check_cargo_put_response(response_json: dict) -> str:
    return __assert(response_json, get_cargo_put_response_example())


def check_cargo_get_id_response(response_json: dict) -> str:
    response_json['car_numbers'] = []
    return __assert(response_json, get_cargo_get_id_response_example())


def check_cargo_get_all_response(response_json: list) -> str:
    assert isinstance(response_json, list)
    response_json = response_json[0]
    response_json['nearest_cars_amount'] = 0
    return __assert(response_json, get_cargo_get_all_response_example())


def check_location(location: dict) -> str:
    assert isinstance(location, dict)
    assert isinstance(location['id'], int)
    assert isinstance(location['zip'], str)
    assert isinstance(location['city'], str)
    assert isinstance(location['lat'], str)
    assert isinstance(location['lng'], str)
    return 'DONE'


def check_car(car: dict) -> str:
    assert isinstance(car, dict)
    assert isinstance(car['id'], int)
    assert isinstance(car['weight'], int)
    assert isinstance(car['number'], str)
    return check_location(car['car_location'])


def check_cars(cars: list) -> str:
    assert isinstance(cars, list)
    assert len(cars) == 20
    assert cars == sorted(cars, key=lambda car: car['id'])
    for car in cars:
        res = check_car(car)
    return res