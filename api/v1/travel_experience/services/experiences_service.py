from ..models.experience import Experience
from db.client import db, client

collection = db.experiences


async def list_all():
    cursor = collection.find({})

    documents = await cursor.to_list(length=None)

    return documents
