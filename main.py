from fastapi import FastAPI
from api import v1
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(v1.api_v1_router)
