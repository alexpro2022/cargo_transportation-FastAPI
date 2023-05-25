from fastapi import APIRouter

from app.api.endpoints import car, cargo, location

main_router = APIRouter()


for endpoint in (car, cargo, location):
    main_router.include_router(endpoint.router)
