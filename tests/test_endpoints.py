from http import HTTPStatus

from .fixtures.data import client  # , URLS
from .utils import check_car


def test_get_cars_endpoint():
    response = client.get('/car/')
    response.status_code == HTTPStatus.OK
    cars = response.json()
    assert isinstance(cars, list)
    assert len(cars) == 20
    assert cars == sorted(cars, key=lambda car: car['id'])
    for car in cars:
        check_car(car)


def test_put_car_endpoint():
    URL = '/car/1'
    invalid_zip = {"current_zip": "strin"}
    invalid_zip_length = (
        {"current_zip": "stri"},
        {"current_zip": "string"},
    )
    valid_json = {"current_zip": "33556"}

    for invalid_method in (
        client.get,
        client.delete,
    ):
        assert invalid_method(URL).status_code == HTTPStatus.METHOD_NOT_ALLOWED

    assert client.put('/car/1', json=invalid_zip).status_code == HTTPStatus.NOT_FOUND
    for json in invalid_zip_length:
        assert client.put('/car/1', json=json).status_code == HTTPStatus.UNPROCESSABLE_ENTITY

    response = client.put('/car/1', json=valid_json)
    assert response.status_code == HTTPStatus.OK


'''def test_valid_urls():
    for prefix, endpoints in URLS.items():
        for endpoint in endpoints:
            url = prefix + endpoint
            response = client.get(url)
            assert response.status_code == HTTPStatus.OK, url
            # assert isinstance(response.json(), list | float)


def test_invalid_prefix():
    for prefix in PREFIXES:
        invalid_prefix = prefix[:-1] if prefix else ' '
        for endpoint, filter in ENDPOINTS:
            for currency in CURRENCIES:
                url = get_url(invalid_prefix, endpoint, QUERY_TICKER, currency, filter)
                response = client.get(url)
                assert response.status_code == HTTPStatus.NOT_FOUND, url'''


'''def test_invalid_endpoint():
    for endpoint, filter in ENDPOINTS:
        invalid_endpoint = endpoint[:-1] if endpoint else ' '
        for currency in CURRENCIES:
            url = get_url(PREFIX, invalid_endpoint, QUERY_TICKER, currency, filter)
            response = client.get(url)
            assert response.status_code == HTTPStatus.NOT_FOUND, url


def test_invalid_query_sintax():
    invalid_ticker = QUERY_TICKER.replace('c', '') if QUERY_TICKER else ' '
    for endpoint, filter in ENDPOINTS:
        for currency in CURRENCIES:
            url = get_url(PREFIX, endpoint, invalid_ticker, currency, filter)
            response = client.get(url)
            assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, url


def test_invalid_currency():
    for endpoint, filter in ENDPOINTS:
        for currency in CURRENCIES:
            invalid_currency = currency[:-1] if currency else ' '
            url = get_url(PREFIX, endpoint, QUERY_TICKER, invalid_currency, filter)
            response = client.get(url)
            assert response.status_code == HTTPStatus.NOT_FOUND, url
            assert response.json() == {'detail': 'Введен неверный тикер валюты - проверьте параметры запроса.'}, url


def test_invalid_filter_sintax():
    invalid_filter = FILTER_BY_DATES.format(NOW, NOW).replace('_', '')
    for currency in CURRENCIES:
        url = get_url(PREFIX, PRICES, QUERY_TICKER, currency, invalid_filter)
        response = client.get(url)
        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, url


def test_invalid_dates():
    for currency in CURRENCIES:
        for dates in INVALID_DATES:
            url = get_url(PREFIX, PRICES, QUERY_TICKER, currency, FILTER_BY_DATES.format(*dates))
            response = client.get(url)
            assert response.status_code == HTTPStatus.BAD_REQUEST, url
            assert response.json() == {'detail': 'Введены неверные даты - проверьте параметры запроса.'}, url


'''
