from urllib import request

from fastapi import Request, APIRouter, Form
from sqlalchemy.orm import sessionmaker
from starlette.responses import RedirectResponse, HTMLResponse

from config import templates
from storage.migrate_up import User, engine

registartion = APIRouter()


@registartion.get("/registration")
def registration(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})


@registartion.post("/regp", response_class=RedirectResponse, status_code=302)
def registr(request: Request, user_name: str = Form(), phone: str = Form(), password: str = Form()):
    if user_name is not None and phone is not None and password is not None:
        SessionLocal = sessionmaker(autoflush=False, bind=engine)
        db = SessionLocal()
        u = User(name=user_name, phone_number=phone, password=password, is_admin_=False)
        db.add(u)
        db.commit()
    return '/set'



