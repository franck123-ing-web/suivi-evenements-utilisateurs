from fastapi import FastAPI

from .database import Base
from .database import engine

from .routes.events import router

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="Suivi des événements utilisateurs",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "API de suivi des événements utilisateurs"
    }