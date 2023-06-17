import csv

import pytest_asyncio

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.db import Base, get_async_session, settings
from app.core.init_db.utils import get_random_car_number, get_random_location, get_random_weight
from app.main import app
from app.models.car import Car
from app.models.location import Location

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(
    class_=AsyncSession, autocommit=False, autoflush=False, bind=engine)


def load_locations():
    columns = [column.key for column in Location.__table__.columns]
    with open(
        'app/core/init_db/data/uszips.csv', encoding='utf-8', newline=''
    ) as csv_file:
        csvreader = csv.DictReader(csv_file, quotechar='"')
        return [Location(**{key: value for key, value in row.items()
                            if key in columns}) for row in csvreader]


def load_cars():
    return [Car(
        number=get_random_car_number(),
        current_location=get_random_location(),
        weight=get_random_weight(),
    ) for i in range(20)]


async def load_db():
    async with TestingSessionLocal() as session:
        locations = load_locations()
        settings.set_locations_amount(len(locations))
        for test_data in (locations, load_cars()):
            session.add_all(set(test_data))
            await session.commit()


@pytest_asyncio.fixture(autouse=True)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await load_db()
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def override_get_async_session():
    async with TestingSessionLocal() as session:
        yield session

app.dependency_overrides[get_async_session] = override_get_async_session
