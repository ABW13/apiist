from fastapi import FastAPI

from app.config import settings
from app.routers import books, recipes

app = FastAPI(
    title=settings.app_name,
    description="A properly structured FastAPI application",
    version="0.1.0",
)

# Each router carries its own prefix and tags, so main.py just attaches them.
app.include_router(books.router)
app.include_router(recipes.router)


@app.get("/")
def root():
    return {"app": settings.app_name, "docs": "/docs"}