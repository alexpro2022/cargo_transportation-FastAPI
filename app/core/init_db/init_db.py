import csv

from app.models.location import Location
from app.models.car import Car
from app.core.init_db.utils import (
    get_random_location, get_random_car_number, get_random_weight, load)


@load
def load_locations():
    columns = [column.key for column in Location.__table__.columns]
    with open(
        'app/core/init_db/data/uszips.csv', encoding='utf-8', newline=''
    ) as csv_file:
        csvreader = csv.DictReader(csv_file, quotechar='"')
        return [Location(**{key: value for key, value in row.items()
                            if key in columns}) for row in csvreader]


@load
def load_cars():
    return [Car(
        number=get_random_car_number(),
        current_location=get_random_location(),
        weight=get_random_weight(),
    ) for i in range(20)]


async def load_data():
    await load_locations()
    await load_cars()
