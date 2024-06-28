from ..models.experience import Experience
from db.client import db, client

collection = db.experiences


async def list_all():
    cursor = collection.find({})

    documents = await cursor.to_list(length=None)

    return documents

async def create(data: Experience):
    result = await collection.insert_one(data.dict())

    return str(result.inserted_id)
