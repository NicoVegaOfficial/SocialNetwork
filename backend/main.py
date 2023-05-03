from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import database

app = FastAPI()

origins = [
   "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Data_User(BaseModel):
    username: str
    email: str
    password: str


class User(BaseModel):
    username: str
    password: str

class Post(BaseModel):
    userid: int
    contenido: str

class DeletePost(BaseModel):
    id: str

@app.post("/login/")
async def login(user: User):
    if (database.valid_user(user.username, user.password) == True):
        return {"user": "valid"}
    else:
        return {"user": "error"}

@app.get("/user/{username}/")
async def user(username: str):
    return database.search_user(username)


@app.post("/adduser/")
async def add_user(data_User: Data_User):
    if (database.add_user(data_User.username, data_User.email, data_User.password) == True):
        return {"Registro": "Valido"}
    else:
        return {"Registro": "error"}

@app.post("/addpost/")
async def add_post(post: Post):
    return database.post_up(post.userid, post.contenido)


@app.delete("/deletepost/")
async def delete_post(post: DeletePost):
    return database.delete_post(post.id)
