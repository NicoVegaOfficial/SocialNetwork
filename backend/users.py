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

class Token(BaseModel):
    id_access : str

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
    

@app.post("/valid_token/")
async def id_session(token: str = Depends(oauth2)):
    if (database.id_session(token)):
        item = {"Token": "Valido"}
        return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content=item)
    else:
        item = {"Token": "No valido"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=item)

@app.post("/id_user/")
async def id_user(token: Token):
    id_user = database.id_session(token.id_access)
    if (id_user != None):
        item = {"Id": id_user[0]}
        return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content=item)
    else:
        item = {"Id": "error"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=item)