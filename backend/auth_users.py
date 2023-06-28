from fastapi import APIRouter
from pydantic import BaseModel
import database

app = APIRouter()

class User(BaseModel):
    username: str
    password: str

class Data_User(User):
    email: str
