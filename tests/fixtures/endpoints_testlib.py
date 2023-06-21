from http import HTTPStatus
from typing import Any, TypeAlias

from httpx import Response
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

Method: TypeAlias = Response
Methods: TypeAlias = tuple[Method]
PathParam: TypeAlias = int | str | None
QueryParams: TypeAlias = dict[str:str] | None
Payload: TypeAlias = dict[str:str] | None


def get_invalid_str() -> str:
    return ('', ' ', '-invalid-')


def get_invalid_int() -> str:
    return (0, -1, 10**12)


def get_invalid_dict_keys(original: dict) -> tuple[dict]:
    dicts = []
    for key in original:
        for invalid_key in ('', ' ', '-invalid-'):
            dd = original.copy()
            value = dd.pop(key)
            dd[invalid_key] = value
            dicts.append(dd)
    return tuple(dicts)


def get_invalid(item: int | str | dict) -> tuple[int | str | dict]:
    if isinstance(item, int):
        return get_invalid_int()
    if isinstance(item, str):
        return get_invalid_str()
    if isinstance(item, dict):
        return get_invalid_dict_keys(item)


def strip_slashes(item: str) -> str:
    if item and item[0] == '/':
        item = item[1:]
    if item and item[-1] == '/':
        item = item[:-1]
    return item


def create_endpoint(endpoint: str, path_param: PathParam) -> str:
    if endpoint in ('/', '//'):
        if path_param is not None:
            return f'/{strip_slashes(str(path_param))}/'
        return '/'
    if path_param is not None:
        return f'/{strip_slashes(endpoint)}/{strip_slashes(str(path_param))}/'
    return f'/{strip_slashes(endpoint)}/'


def get_method(method: str) -> Method:
    match method.upper():
        case 'GET':
            return client.get
        case 'POST':
            return client.post
        case 'PUT':
            return client.put
        case 'PATCH':
            return client.patch
        case 'DELETE':
            return client.delete


def get_response(
    method: str,
    endpoint: str,
    path_param: int | str | None = None,
    query_params: dict[str:str] | None = None,
    payload: dict[str:str] | None = None,
) -> Response:
    endpoint = create_endpoint(endpoint, path_param)
    method = get_method(method)
    if payload is not None and query_params is not None:
        return method(endpoint, params=query_params, json=payload)
    if payload is not None:
        return method(endpoint, json=payload)
    if query_params is not None:
        return method(endpoint, params=query_params)
    return method(endpoint)


def assert_response(
    status_code: int,
    method: str,
    endpoint: str,
    path_param: int | str | None = None,
    query_params: dict[str:str] | None = None,
    payload: dict[str:str] | None = None,
) -> Response:
    response = get_response(method, endpoint, path_param, query_params, payload)
    assert response.status_code == status_code, \
        f'{response.status_code} -> {method}({create_endpoint(endpoint, path_param)}, {query_params}, {payload})'
    return response


def __dummy_func(response_json) -> str:
    return 'DONE'


def valid_values_standard_tests(
    method: str,
    endpoint: str,
    path_param: int | str | None = None,
    query_params: dict[str:str] | None = None,
    payload: dict[str:str] | None = None,
    func_check_valid_response: Any | None = None,
    msg_invalid_path_param: str | None = None,
) -> None:

    # valid_request_test
    response = assert_response(HTTPStatus.OK, method, endpoint, path_param, query_params, payload)
    if func_check_valid_response is None:
        func_check_valid_response = __dummy_func
    assert func_check_valid_response(response.json()) == 'DONE'

    # invalid_endpoint_test
    for invalid_endpoint in get_invalid(endpoint):
        assert_response(HTTPStatus.NOT_FOUND, method, invalid_endpoint, path_param, query_params, payload)

    # invalid_path_param_test
    if path_param is not None:
        for invalid_path_param in get_invalid(path_param):
            response = assert_response(HTTPStatus.NOT_FOUND, method, endpoint, invalid_path_param, query_params, payload)
            if msg_invalid_path_param is not None:
                assert response.json() == {'detail': msg_invalid_path_param}, response.json()

    # invalid_query_params_keys_test
    if query_params is not None:
        for invalid_keys_query_params in get_invalid(query_params):
            assert_response(HTTPStatus.UNPROCESSABLE_ENTITY, method, endpoint, path_param, invalid_keys_query_params, payload)

    # invalid_payload_keys_test
    if payload is not None:
        for invalid_keys_payload in get_invalid(payload):
            assert_response(HTTPStatus.UNPROCESSABLE_ENTITY, method, endpoint, path_param, query_params, invalid_keys_payload)


def invalid_methods_test(
    invalid_methods: tuple[str],
    endpoint: str,
    path_param: int | str | None = None,
) -> None:
    for invalid_method in invalid_methods:
        assert_response(HTTPStatus.METHOD_NOT_ALLOWED, invalid_method, endpoint, path_param)