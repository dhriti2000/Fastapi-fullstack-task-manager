from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from database import SessionLocal
from models import User

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
def login(request: Request, username: str = Form(), password: str = Form()):
    db = SessionLocal()
    try:
        user = db.query(User).filter(
            User.username == username,
            User.password == password
        ).first()
    finally:
        db.close()

    if not user:
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "Invalid credentials"}
        )

    response = RedirectResponse("/", status_code=302)
    response.set_cookie("user", username)
    return response


@router.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register")
def register(username: str = Form(), password: str = Form()):
    db = SessionLocal()
    try:
        db.add(User(username=username, password=password))
        db.commit()
    finally:
        db.close()

    return RedirectResponse("/login", status_code=302)


@router.get("/logout")
def logout():
    response = RedirectResponse("/login", status_code=302)
    response.delete_cookie("user")
    return response
