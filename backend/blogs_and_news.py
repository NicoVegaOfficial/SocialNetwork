from fastapi import APIRouter
from pydantic import BaseModel
import database

app = APIRouter()

class Id_post(BaseModel):
    userid: str

class Post(Id_post):
    contenido: str

class Delete_Post(BaseModel):
    id: str

@app.get("/lastpost/{post_id}")
async def last_post(post_id: int):
    return database.get_post(post_id)

@app.post("/addpost/")
async def add_post(post: Post):
    return database.post_up(post.userid, post.contenido)


@app.delete("/deletepost/")
async def delete_post(post: Delete_Post):
    return database.delete_post(post.id)
