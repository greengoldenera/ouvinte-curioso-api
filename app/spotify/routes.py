from fastapi import APIRouter, HTTPException, Request

from app.auth.session import require_session_tokens
from app.spotify.client import get_currently_playing
from app.spotify.mapper import map_currently_playing_payload
from app.spotify.schemas import CurrentlyPlayingDto

router = APIRouter(prefix="/me/player", tags=["spotify"])


@router.get("/currently-playing")
async def currently_playing(request: Request) -> CurrentlyPlayingDto:
    tokens = require_session_tokens(request)
    response = await get_currently_playing(tokens["access_token"])

    if response.status_code == 204:
        return CurrentlyPlayingDto(is_playing=False)

    if response.status_code == 401:
        raise HTTPException(status_code=401, detail="Spotify token expired")

    if response.status_code == 403:
        raise HTTPException(status_code=403, detail="Spotify permission denied")

    if response.status_code == 429:
        raise HTTPException(status_code=429, detail="Spotify rate limit")

    response.raise_for_status()
    return map_currently_playing_payload(response.json())
