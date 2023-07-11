from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import database
import secrets

app = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    password: str

class Data_User(User):
    email: str

@app.post("/login/")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    if (database.valid_user(form.username, form.password) == True):
        session_id = secrets.token_hex(32)
        database.active_session(session_id, database.get_user_id(form.username)) 
        return {"access_token": session_id, "token_type": "bearer"}
    else:
        return {"session_id": None}

@app.get("/user/{username}/")
async def user(username: str):
    return database.search_user(username)


@app.post("/adduser/")
async def add_user(data_User: Data_User):
    if (database.add_user(data_User.username, data_User.email, data_User.password) == True):
        return {"Registro": "Valido"}
    else:
        return {"Registro": "error"}

async def current_user(token: str = Depends(oauth2)):
    return database.valid_session(token)

@app.post("/valid_token/")
async def valid_token(token: str = Depends(current_user)):
    if (database.valid_session(token)):
        return True
    else:
        return False
