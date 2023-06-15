from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI

from app.api.routers import main_router
from app.core import load_data, settings
from app.crud.car import car_crud


app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
)

app.include_router(main_router)


@app.on_event('startup')
async def startup():
    await load_data()
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        car_crud.update_cars_location,
        settings.SCHEDULER_TRIGGER,
        seconds=settings.SCHEDULER_INTERVAL,
    )
    scheduler.start()
