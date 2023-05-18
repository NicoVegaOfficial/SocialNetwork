from fastapi import APIRouter
from pydantic import BaseModel
import database

app = APIRouter()

class Post(BaseModel):
    userid: int
    contenido: str

class DeletePost(BaseModel):
    id: str


@app.post("/addpost/")
async def add_post(post: Post):
    return database.post_up(post.userid, post.contenido)


@app.delete("/deletepost/")
async def delete_post(post: DeletePost):
    return database.delete_post(post.id)
