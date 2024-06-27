from fastapi import FastAPI
from api import v1

app = FastAPI()

app.include_router(v1.api_v1_router)
