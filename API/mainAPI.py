from fastapi import FastAPI
from API.routes.get_routes import router as get_router
from API.routes.post_routes import router as post_router

app = FastAPI()

app.include_router(get_router)
app.include_router(post_router)
