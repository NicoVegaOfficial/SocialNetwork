from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import users
import blogs_and_news

app = FastAPI()

#Configuraciones
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

#Routers
app.include_router(users.app)
app.include_router(blogs_and_news.app)
