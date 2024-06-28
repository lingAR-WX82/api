from fastapi import APIRouter
from typing import List
from ..services import experiences_service as service
from ..models.experience import Experience

router = APIRouter()


@router.get("/", response_model=List[Experience])
async def get_experiences():
    documents = await service.list_all()
    return documents

@router.post("/")
async def create_experience(data: Experience):
    result = await service.create(data)
    return result
