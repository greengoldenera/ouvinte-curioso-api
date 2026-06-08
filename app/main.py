from fastapi import FastAPI

from app.auth.routes import router as auth_router
from app.spotify.routes import router as spotify_router

app = FastAPI(title="Ouvinte Curioso API")

app.include_router(auth_router)
app.include_router(spotify_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "ouvinte-curioso-api",
    }
