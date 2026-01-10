from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from database import SessionLocal
from models import Todo

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/")
def home(request: Request):
    user = request.cookies.get("user")
    if not user:
        return RedirectResponse("/login", status_code=302)

    db = SessionLocal()
    try:
        todos = db.query(Todo).filter(Todo.owner == user).all()
    finally:
        db.close()

    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,   # 🔴 REQUIRED
            "todos": todos,       # 🔴 must match template
            "user": user
        }
    )


@router.get("/add")
def add_page(request: Request):
    if not request.cookies.get("user"):
        return RedirectResponse("/login", status_code=302)

    return templates.TemplateResponse(
        "add_todo.html",
        {"request": request}
    )


@router.post("/add")
def add_task(title: str = Form(), description: str = Form(), request: Request = None):
    user = request.cookies.get("user")
    if not user:
        return RedirectResponse("/login", status_code=302)

    db = SessionLocal()
    try:
        db.add(Todo(title=title, description=description, owner=user))
        db.commit()
    finally:
        db.close()

    return RedirectResponse("/", status_code=302)
