from fastapi import FastAPI

from app.api.routers import main_router
from app.core.config import settings
from app.core.init_db import load_locations
# from app.core.init_db import fill_data

app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
)

app.include_router(main_router)


@app.on_event('startup')
async def startup():
    await load_locations()
    # await check_db_connection()
