from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from database import Base, engine
from routers.auth import router as auth_router
from routers.todo import router as todo_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth_router)
app.include_router(todo_router)
