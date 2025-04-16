from Backend import database as db
from fastapi import APIRouter, Form

router = APIRouter()

@router.post("/UploadRecipe")
def UploadRecipe(
        Target: str = Form(...),
        title: str = Form(...),
        steps: str = Form(...)
    ):
    data = {"title": title, "steps": steps}
    db.AddToCollection(collection_name=Target, data=data)
    return {"status": "Received", "data": data}
