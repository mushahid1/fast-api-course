from fastapi import FastAPI
from . import models 
from .database import engine
from .routers import post, user, auth, votes
from fastapi.middleware.cors import CORSMiddleware

# As we have alembi installed nnow we don't need to create models/tables
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Specify perticular domains to allow to interact with APIs.
# If want to allow all (which is not recommended) just add asterisk
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")
def root():
    return {"message": "Welcome to my fast api!!!"}