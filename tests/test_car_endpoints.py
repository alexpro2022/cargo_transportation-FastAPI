from http import HTTPStatus

from .fixtures.data import DELETE, GET, PATCH, POST, PUT
from .fixtures.endpoints_testlib import (assert_response,
                                         invalid_methods_test,
                                         valid_values_standard_tests)
from .utils import check_car, check_cars

# === VALID ===
CAR_ENDPOINT = 'car'
CAR_ID = 11
CURRENT_ZIP = 'current_zip'
ZIP_CODE = '33556'
CAR_LOCATION = {
    "id": 11111,
    "zip": "33556",
    "state_name": "Florida",
    "city": "Odessa",
    "lat": "28.17029",
    "lng": "-82.59264"
}


def check_car_for_zip(car):
    check_car(car)
    assert car['car_location'] == CAR_LOCATION, (car['car_location'], CAR_LOCATION)
    return 'DONE'


def invalid_methods_for_car_endpoints() -> None:
    for case in (
        ((DELETE, PATCH, POST, PUT), CAR_ENDPOINT),
        ((DELETE, GET, PATCH, POST), CAR_ENDPOINT, CAR_ID),
    ):
        invalid_methods_test(*case)


def valid_values_standard_tests_for_car_endpoints() -> None:
    msg_invalid_path_param = 'Машина не найдена, проверьте ID или параметры запроса.'
    for case in (
        (GET, CAR_ENDPOINT, None, None, None, check_cars),
        (PUT, CAR_ENDPOINT, CAR_ID, None, {CURRENT_ZIP: ZIP_CODE}, check_car_for_zip, msg_invalid_path_param),
    ):
        valid_values_standard_tests(*case)


def car_invalid_zip_value():
    msg = 'Локация не найдена - неверный location_id или zip-код.'
    for invalid_zip in ('12345',):
        response = assert_response(HTTPStatus.NOT_FOUND, PUT, CAR_ENDPOINT, CAR_ID, payload={CURRENT_ZIP: invalid_zip})
        assert response.json() == {'detail': msg}, response.json()


def car_invalid_zip_length():
    for invalid_zip in ('', ' ', '1234', '123456'):
        assert_response(HTTPStatus.UNPROCESSABLE_ENTITY, PUT, CAR_ENDPOINT, CAR_ID, payload={CURRENT_ZIP: invalid_zip})


def test_car_endpoints():
    valid_values_standard_tests_for_car_endpoints()
    invalid_methods_for_car_endpoints()
    car_invalid_zip_value()
    car_invalid_zip_length()
