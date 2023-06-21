GET = 'get'
POST = 'post'
PUT = 'put'
PATCH = 'patch'
DELETE = 'delete'

_FIRST_POST_PAYLOAD = {
    "delivery_zip": "00602",
    "current_zip": "00601",
    "description": "description",
    "weight": 100
}
_FIRST_PUT_PAYLOAD = {
    "description": "put",
    "weight": 999
}
_FIRST_CARGO_GENERIC = {
    "pick_up": {
        "id": 1,
        "zip": "00601",
        "state_name": "Puerto Rico",
        "city": "Adjuntas",
        "lat": "18.18027",
        "lng": "-66.75266"
    },
    "delivery": {
        "id": 2,
        "zip": "00602",
        "state_name": "Puerto Rico",
        "city": "Aguada",
        "lat": "18.36075",
        "lng": "-67.17541"
    },
    "weight": 100,
    "description": "description",
    "nearest_cars_amount": 0,
    "car_numbers": []
}

_SECOND_POST_PAYLOAD = {
    "delivery_zip": "33556",
    "current_zip": "15049",
    "description": "description",
    "weight": 500
}
_SECOND_CARGO_GENERIC = {
    "pick_up": {
        "id": 4444,
        "zip": "15049",
        "state_name": "Pennsylvania",
        "city": "Harwick",
        "lat": "40.55545",
        "lng": "-79.80366"
    },
    "delivery": {
        "id": 11111,
        "zip": "33556",
        "state_name": "Florida",
        "city": "Odessa",
        "lat": "28.17029",
        "lng": "-82.59264"
    },
    "weight": 500,
    "description": "description",
    "nearest_cars_amount": 0,
    "car_numbers": []
}

CARGO_GENERIC = _FIRST_CARGO_GENERIC
POST_PAYLOAD = _FIRST_POST_PAYLOAD
PUT_PAYLOAD = _FIRST_PUT_PAYLOAD


def get_cargo_post_response_example():
    cargo = CARGO_GENERIC.copy()
    cargo.pop('nearest_cars_amount')
    cargo.pop('car_numbers')
    return cargo


def get_cargo_put_response_example():
    cargo = get_cargo_post_response_example()
    cargo['description'] = PUT_PAYLOAD['description']
    cargo['weight'] = PUT_PAYLOAD['weight']
    return cargo


def get_cargo_get_id_response_example():
    cargo = get_cargo_put_response_example()
    cargo['car_numbers'] = []
    return cargo


def get_cargo_get_all_response_example():
    cargo = CARGO_GENERIC.copy()
    cargo.pop('weight')
    cargo.pop('description')
    cargo.pop('car_numbers')
    return cargo