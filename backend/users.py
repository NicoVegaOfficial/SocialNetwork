from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import database
import secrets

app = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    email: str
    password: str

@app.post("/login/")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    if (database.valid_user(form.username, form.password) == True):
        session_id = secrets.token_hex(32)
        database.active_session(session_id, database.get_user_id(form.username)) 
        item = {"access_token": session_id, "token_type": "bearer"}
        return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content=item)
    else:
        item = {"session_id": None}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=item)

@app.get("/user/{username}/")
async def user(username: str):
    return database.search_user(username)

@app.post("/adduser/")
async def add_user(data_User: User):
    if (database.add_user(data_User.username, data_User.email, data_User.password) == True):
        item = {"Registro": "Valido"}
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)
    else:
        item = {"Registro": "error"}
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=item)
    
async def current_user(token: str = Depends(oauth2)):
    return database.valid_session(token)

@app.post("/valid_token/")
async def valid_token(token: str = Depends(current_user)):
    if (database.valid_session(token)):
        return True
    else:
        return False
