from http import HTTPStatus

from .fixtures.data import DELETE, GET, PATCH, POST, PUT, POST_PAYLOAD, PUT_PAYLOAD
from .fixtures.endpoints_testlib import (assert_response,
                                         invalid_methods_test,
                                         valid_values_standard_tests)
from .utils import (check_cargo_get_all_response,
                    check_cargo_get_id_response,
                    check_cargo_post_response,
                    check_cargo_put_response,
                    empty_list)

CARGO_ENDPOINT = 'cargo'
CARGO_ID = 1


def valid_values_standard():
    msg_invalid_path_param = 'Груз не найден, проверьте ID или параметры запроса.'
    for case in (
        (GET, CARGO_ENDPOINT, None, None, None, empty_list),
        (POST, CARGO_ENDPOINT, None, None, POST_PAYLOAD, check_cargo_post_response),
        (GET, CARGO_ENDPOINT, None, None, None, check_cargo_get_all_response),
        (PUT, CARGO_ENDPOINT, CARGO_ID, None, PUT_PAYLOAD, check_cargo_put_response),
        (GET, CARGO_ENDPOINT, CARGO_ID, None, None, check_cargo_get_id_response),
        (DELETE, CARGO_ENDPOINT, CARGO_ID),
    ):
        valid_values_standard_tests(*case, msg_invalid_path_param=msg_invalid_path_param)


def invalid_methods():
    for case in (
        ((PUT, PATCH, DELETE), CARGO_ENDPOINT),
        ((PATCH, POST), CARGO_ENDPOINT, CARGO_ID),
    ):
        invalid_methods_test(*case)


def cargo_put_payload_invalid_weight():
    invalid_payload = PUT_PAYLOAD.copy()
    for invalid_weigth in (-1, 0, 1001):
        invalid_payload['weight'] = invalid_weigth
        assert_response(HTTPStatus.UNPROCESSABLE_ENTITY, PUT, CARGO_ENDPOINT, CARGO_ID, payload=invalid_payload)


def cargo_post_payload_invalid_weight():
    invalid_payload = POST_PAYLOAD.copy()
    for invalid_weigth in (-1, 0, 1001):
        invalid_payload['weight'] = invalid_weigth
        assert_response(HTTPStatus.UNPROCESSABLE_ENTITY, POST, CARGO_ENDPOINT, payload=invalid_payload)


def cargo_post_payload_invalid_zip_value():
    msg = 'Локация не найдена - неверный location_id или zip-код.'
    for invalid_zip in ('12345',):
        for key in ('delivery_zip', 'current_zip'):
            invalid_payload = POST_PAYLOAD.copy()
            invalid_payload[key] = invalid_zip
            response = assert_response(HTTPStatus.NOT_FOUND, POST, CARGO_ENDPOINT, payload=invalid_payload)
            assert response.json() == {'detail': msg}, response.json()


def cargo_post_payload_invalid_zip_length():
    for invalid_zip in ('', ' ', '1234', '123456'):
        for key in ('delivery_zip', 'current_zip'):
            invalid_payload = POST_PAYLOAD.copy()
            invalid_payload[key] = invalid_zip
            assert_response(HTTPStatus.UNPROCESSABLE_ENTITY, POST, CARGO_ENDPOINT, payload=invalid_payload)


def test_cargo_endpoints():
    invalid_methods()
    valid_values_standard()
    cargo_put_payload_invalid_weight()
    cargo_post_payload_invalid_weight()
    cargo_post_payload_invalid_zip_value()
    cargo_post_payload_invalid_zip_length()