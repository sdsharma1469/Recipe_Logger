from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from Backend import database as db

templates = Jinja2Templates(directory="Frontend/templates")

router = APIRouter()

@router.get("/home")
def render_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "name": "Shaunak"})

@router.get("/")
def default():
    return {"hello"}

@router.get("/UploadRecipe")
def UploadPage(request: Request):
    return templates.TemplateResponse("UploadRecipe.html", {"request": request, "name": "Shaunak"})
