from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_experiences():
    return [{"name": "Trekking in the Himalayas"}, {"name": "Sunbathing in the Caribbean"}]
