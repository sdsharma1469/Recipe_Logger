from fastapi import FastAPI
from API.routes.get_routes import get_routes, post_routes

app = FastAPI()

app.include_router(get_routes.router)
app.include_router(post_routes.router)
