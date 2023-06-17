

def check_car(car):
    assert isinstance(car, dict)
    assert isinstance(car['id'], int)
    assert isinstance(car['weight'], int)
    assert isinstance(car['number'], str)
    assert isinstance(car['car_location'], dict)
    assert isinstance(car['car_location']['id'], int)
    assert isinstance(car['car_location']['zip'], str)
    assert isinstance(car['car_location']['state_name'], str)
    assert isinstance(car['car_location']['city'], str)
    assert isinstance(car['car_location']['lat'], str)
    assert isinstance(car['car_location']['lng'], str)


'''import random
from typing import Any, Iterable

from httpx import Response

from .fixtures.data import ALL, client, PREFIX, QUERY_TICKER
from .fixtures.test_db_data import BTC_TEST_DATA, ETH_TEST_DATA


def get_url(prefix: str, endpoint: str, query: str, currency: str, filter=None) -> str:
    filter = '' if filter is None else filter
    return prefix + endpoint + query + currency + filter


def get_sorted(arr: Iterable, each_key: str = 'timestamp', reverse: bool = False) -> list[Any]:
    return sorted([each for each in arr], key=lambda each: each[each_key], reverse=reverse)


def get_all(currency: str) -> Response:
    url = get_url(PREFIX, ALL, QUERY_TICKER, currency)
    return client.get(url)


def compare(response_data, test_data):
    assert response_data['name'] == test_data['name']
    assert response_data['price'] == test_data['price']
    assert response_data['timestamp'] == test_data['timestamp']


def check_data(response_data, test_data):
    assert len(response_data) == len(test_data)
    for i in range(len(response_data)):
        compare(response_data[i], test_data[i])





def get_randome_timestamps(test_data: list[dict]) -> tuple[int, int]:
    timestamps = [test_data[random.randint(0, len(test_data) - 1)]['timestamp'] for _ in range(2)]
    return min(*timestamps), max(*timestamps)


def get_test_prices(test_data: list[dict], from_: int, to_: int) -> list[float]:
    return [data['price'] for data in test_data if from_ <= data['timestamp'] <= to_]


def get_test_data(currency):
    if currency == 'BTC':
        return BTC_TEST_DATA
    elif currency == 'ETH':
        return ETH_TEST_DATA'''