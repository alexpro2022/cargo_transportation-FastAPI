import csv

from sqlalchemy.exc import IntegrityError

from app.core.db import AsyncSessionLocal
from app.models.location import Location
from app.models.car import Car


async def load(data: list):
    # [print(locations[i]) for i in range(10)]
    session = AsyncSessionLocal()
    session.add_all(data)
    try:
        print('Loading data ...')
        await session.commit() 
    except IntegrityError:
        print('Data has already been loaded ... exiting')
        await session.rollback()
    print('Data has successfully been loaded')    


async def load_locations():
    columns = [column.key for column in Location.__table__.columns]
    with open(
        'app/core/data/uszips.csv', encoding='utf-8', newline=''
    ) as csv_file:
        csvreader = csv.DictReader(csv_file, quotechar='"')
        locations = [Location(**{key: value for key, value in row.items() if key in columns}) for row in csvreader]
        await load(locations)


async def load_cars():
    cars = []
    await load(cars)

