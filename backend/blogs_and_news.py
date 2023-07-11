from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
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
    if (database.post_up(post.userid, post.contenido) == True):
        item = {"Status": "Ok"}
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)
    else:
        item = {"Status": "Error"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED , content=item)


@app.delete("/deletepost/")
async def delete_post(post: Delete_Post):
    if (database.delete_post(post.id)):
        item = {"Status": "Deleted"}
        return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content=item)
    else:
        item = {"Status": "Error"}
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED , content=item)

