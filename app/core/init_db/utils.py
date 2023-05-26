import random
from string import ascii_uppercase

from sqlalchemy.exc import IntegrityError

from app.core.config import settings
from app.core.db import AsyncSessionLocal
from app.models.location import Location


def load(func):
    async def wrapper(*args, **kwargs):
        data_name = '=None='
        data = func(*args, **kwargs)
        if data:
            data_name = f'={data[0].__class__.__name__.lower()}s='
            if isinstance(data[0], Location):
                settings.set_locations_amount(len(data))
        session = AsyncSessionLocal()
        session.add_all(data)
        try:
            print(f'Loading data {data_name} ...')
            await session.commit()
        except IntegrityError:
            print(f'Data {data_name} has already been loaded ... exiting')
            await session.rollback()
        else:
            print(f'Data {data_name} has successfully been loaded')
    return wrapper


def get_random_location():
    return random.randint(1, settings.get_locations_amount())


def get_random_car_number():
    return ''.join((
        str(random.randint(*settings.CAR_NUMBER_RANGE)),
        random.choice(ascii_uppercase),
    ))


def get_random_weight():
    return random.randint(*settings.WEIGHT_RANGE)
