from fastapi import APIRouter

from .travel_experience import travel_experience_router

api_v1_router = APIRouter(prefix="/api/v1")

api_v1_router.include_router(travel_experience_router)

