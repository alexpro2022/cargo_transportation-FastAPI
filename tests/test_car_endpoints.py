from http import HTTPStatus

from .fixtures.data import DELETE, GET, PATCH, POST, PUT
from .fixtures.endpoints_testlib import assert_response, invalid_methods_test, valid_values_standard_tests
from .utils import check_car, check_cars

# === VALID ===
CAR_ENDPOINT = 'car'
CAR_INDEX = 11
CURRENT_ZIP = 'current_zip'
ZIP_CODE = "33556"


def invalid_methods_for_car_endpoints() -> None:
    for case in (
        ((DELETE, PATCH, POST, PUT), CAR_ENDPOINT),
        ((DELETE, GET, PATCH, POST), CAR_ENDPOINT, CAR_INDEX),
    ):
        invalid_methods_test(*case)


def valid_values_standard_tests_for_car_endpoints() -> None:
    msg_invalid_path_param = 'Машина не найдена, проверьте ID или параметры запроса.'
    for case in (
        (GET, CAR_ENDPOINT, None, None, None, check_cars),
        (PUT, CAR_ENDPOINT, CAR_INDEX, None, {CURRENT_ZIP: ZIP_CODE}, check_car, msg_invalid_path_param),
    ):
        valid_values_standard_tests(*case)


def car_invalid_zip_value():
    msg = 'Локация не найдена - неверный location_id или zip-код.'
    invalid_zip_value = ('12345',)
    for invalid_zip in invalid_zip_value:
        response = assert_response(HTTPStatus.NOT_FOUND, PUT, CAR_ENDPOINT, CAR_INDEX, payload={CURRENT_ZIP: invalid_zip})
        assert response.json() == {'detail': msg}, response.json()


def car_invalid_zip_length():
    invalid_zip_length = ('', ' ', '1234', '123456')
    for invalid_zip in invalid_zip_length:
        assert_response(HTTPStatus.UNPROCESSABLE_ENTITY, PUT, CAR_ENDPOINT, CAR_INDEX, payload={CURRENT_ZIP: invalid_zip})


def test_car_endpoints():
    valid_values_standard_tests_for_car_endpoints()
    invalid_methods_for_car_endpoints()
    car_invalid_zip_value()
    car_invalid_zip_length()


'''def car_valid():
    valid_requests_test(
        ((client.get,), CAR_ENDPOINT, None, None, None, check_cars),
        ((client.put,), CAR_ENDPOINT, CAR_INDEX, None, PAYLOAD, check_car),
    )


def car_invalid_methods():
    invalid_methods_test(
        ((client.put, client.patch, client.delete, client.post), CAR_ENDPOINT, None),
        ((client.get, client.patch, client.delete, client.post), CAR_ENDPOINT, CAR_INDEX),
    )


def car_invalid_endpoints():
    invalid_endpoints_test(
        ((client.get,), CAR_ENDPOINT),
        ((client.put,), CAR_ENDPOINT),
    )


def car_invalid_index():
    msg = 'Машина не найдена, проверьте ID или параметры запроса.'
    invalid_path_param_test(
        (client.put, CAR_ENDPOINT, CAR_INDEX, None, PAYLOAD, msg),
    )


def car_invalid_zip_value():
    invalid_zip = {"current_zip": "strin"}
    response = client.put(CAR_ENDPOINT + CAR_INDEX, json=invalid_zip)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Введен неверный zip-код - проверьте параметры запроса.'}


def put_car_invalid_zip_length():
    invalid_zip_length = (
        {"current_zip": "stri"},
        {"current_zip": "string"},
        {' ': ' '},
        # {'', ''}  ANALIZE THIS )
    )
    for json in invalid_zip_length:
        assert client.put(CAR_ENDPOINT + CAR_INDEX, json=json).status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def put_car_valid_zip():
    for json in valid_jsons:
        response = client.put(CAR_ENDPOINT + CAR_INDEX, json=json)
        assert response.status_code == HTTPStatus.OK
        updated_car = response.json()
        check_car(updated_car)
        assert updated_car['car_location']['zip'] == json['current_zip


def test_car_endpoints():
    car_valid()
    car_invalid_methods()
    car_invalid_endpoints()
    car_invalid_index()
    # put_car_invalid_zip_length()
    # put_car_invalid_zip_value()
    # put_car_valid_zip()
    # get_cars_endpoint()

'''
