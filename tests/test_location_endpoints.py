from .fixtures.data import DELETE, GET, PATCH, POST, PUT
from .fixtures.endpoints_testlib import invalid_methods_test, valid_values_standard_tests
from .utils import check_location

LOCATION_ENDPOINT = 'location'
LOCATION_ID = 11111


def test_location_endpoint():
    msg = 'Локация не найдена - неверный location_id или zip-код.'
    valid_values_standard_tests(GET, LOCATION_ENDPOINT, LOCATION_ID, func_check_valid_response=check_location, msg_invalid_path_param=msg)
    invalid_methods_test((POST, PUT, PATCH, DELETE), LOCATION_ENDPOINT, LOCATION_ID)
