from datetime import datetime as dt
from http import HTTPStatus

from app.core.config import settings

from .fixtures.data import (FILTER_BY_DATES, LAST_PRICE, PREFIX, PRICES,
                            QUERY_TICKER, client)
from .utils import (check_data, check_item, get_all, get_randome_timestamps,
                    get_sorted, get_test_data, get_test_prices, get_url)


def test_get_all_for_currency():
    for currency in settings.get_currencies():
        response = get_all(currency)
        assert response.status_code == HTTPStatus.OK
        all = response.json()
        assert isinstance(all, list)
        assert all == get_sorted(all, reverse=True)
        for each in all:
            check_item(each, currency)
        check_data(all, get_test_data(currency))


def test_last_price_for_currency():
    for currency in settings.get_currencies():
        url = get_url(PREFIX, LAST_PRICE, QUERY_TICKER, currency)
        response = client.get(url)
        assert response.status_code == HTTPStatus.OK, url
        last_price = response.json()
        assert isinstance(last_price, float), url
        assert last_price == get_all(currency).json()[0]['price'], url


def test_prices():
    for currency in settings.get_currencies():
        for _ in range(100):
            from_, to_ = get_randome_timestamps(get_test_data(currency))
            url = get_url(PREFIX, PRICES, QUERY_TICKER, currency, FILTER_BY_DATES.format(dt.fromtimestamp(from_), dt.fromtimestamp(to_)))
            response = client.get(url)
            assert response.status_code == HTTPStatus.OK
            prices = response.json()
            assert isinstance(prices, list)
            assert prices == get_test_prices(get_test_data(currency), from_, to_)