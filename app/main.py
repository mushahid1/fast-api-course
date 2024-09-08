from fastapi import FastAPI
from . import models 
from .database import engine
from .routers import post, user, auth, votes

# As we have alembi installed nnow we don't need to create models/tables
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")
def root():
    return {"message": "Welcome to my api!!!"}