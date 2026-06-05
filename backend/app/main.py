from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routes.events import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Suivi des événements utilisateurs",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "API de suivi des événements utilisateurs"
    }