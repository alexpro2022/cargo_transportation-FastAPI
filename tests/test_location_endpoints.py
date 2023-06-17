from http import HTTPStatus

from .fixtures.data import client
from .utils import check_location

ENDPOINT = '/location/'
LOCATION_INDEX = '1'


def location_invalid_methods():
    for endpoint, invalid_methods in {
        ENDPOINT + LOCATION_INDEX: (client.post, client.put, client.patch, client.delete)
    }.items():
        for invalid_method in invalid_methods:
            assert invalid_method(endpoint).status_code == HTTPStatus.METHOD_NOT_ALLOWED


def location_invalid_endpoints():
    inv_endpoint = ENDPOINT[:-2] + '/'
    for invalid_endpoint, valid_method in {
        inv_endpoint + LOCATION_INDEX: client.get,
    }.items():
        assert valid_method(invalid_endpoint).status_code == HTTPStatus.NOT_FOUND


def location_valid():
    response = client.get(ENDPOINT + LOCATION_INDEX)
    assert response.status_code == HTTPStatus.OK
    location = response.json()
    check_location(location)


def test_location_endpoints():
    location_invalid_methods()
    location_invalid_endpoints()
    location_valid()
