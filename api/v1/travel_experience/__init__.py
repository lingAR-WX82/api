from fastapi import APIRouter
from .controllers.experiences_controller import router as experiences_router

travel_experience_router = APIRouter()

travel_experience_router.include_router(experiences_router, prefix="/experiences", tags=["Experiences"])
