# Technically started revision on 9/25/2023 @ 7:50 AM - Joining date of Babu.

from fastapi import FastAPI
from . import models
from .database import engine
from .routers import auth, user, post, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware



# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/") #decorator.
def root():
    return {"message": "Welcome come to my API!"}


