from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional


class Experience(BaseModel):
    id: Optional[ObjectId] = Field(alias='_id')
    title: str
    description: str
    latitude: float
    longitude: float

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
