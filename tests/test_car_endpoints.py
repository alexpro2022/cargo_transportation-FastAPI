from http import HTTPStatus

from .fixtures.data import client
from .utils import check_car

URL = '/car/'
CAR_INDEX = '1'


def get_cars_endpoint():
    response = client.get(URL)
    response.status_code == HTTPStatus.OK
    cars = response.json()
    assert isinstance(cars, list)
    assert len(cars) == 20
    assert cars == sorted(cars, key=lambda car: car['id'])
    for car in cars:
        check_car(car)


def put_car_invalid_methods():
    for invalid_method in (
        client.get,
        client.delete,
    ):
        assert invalid_method(URL + CAR_INDEX).status_code == HTTPStatus.METHOD_NOT_ALLOWED


def put_car_invalid_zip():
    invalid_zip = {"current_zip": "strin"}
    response = client.put(URL + CAR_INDEX, json=invalid_zip)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Введен неверный zip-код - проверьте параметры запроса.'}


def put_car_invalid_zip_length():
    invalid_zip_length = (
        {"current_zip": "stri"},
        {"current_zip": "string"},
        {' ': ' '},
    )
    for json in invalid_zip_length:
        assert client.put(URL + CAR_INDEX, json=json).status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def put_car_valid_zip():
    valid_jsons = (
        {"current_zip": "33556"},
        {"current_zip": "00601"},
        {"current_zip": "00602"},
    )
    for json in valid_jsons:
        response = client.put(URL + CAR_INDEX, json=json)
        assert response.status_code == HTTPStatus.OK
        updated_car = response.json()
        check_car(updated_car)
        assert updated_car['car_location']['zip'] == json['current_zip']


def test_car_endpoints():
    get_cars_endpoint()
    put_car_invalid_methods()
    put_car_invalid_zip()
    put_car_invalid_zip_length()
    put_car_valid_zip()