from Backend import database as db
from fastapi import APIRouter, Form

router = APIRouter()

@router.get("/")
def default():
    return {"hello"}

