from Backend import database as db
from fastapi import APIRouter, Form

router = APIRouter()


@router.post("/UploadRecipe") 
def UploadRecipe(Target, data: dict):
    print(type(Target))
    print(type(data))
    db.AddToCollection(collection_name= Target, data= data)
    return {"status": "Received", "data": data}