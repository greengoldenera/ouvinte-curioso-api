from urllib.parse import urlencode

import httpx

from app.core.config import settings


SPOTIFY_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"


def build_authorize_url(state: str) -> str:
    params = {
        "response_type": "code",
        "client_id": settings.spotify_client_id,
        "scope": settings.spotify_scopes,
        "redirect_uri": settings.spotify_redirect_uri,
        "state": state,
    }
    return f"{SPOTIFY_AUTHORIZE_URL}?{urlencode(params)}"


async def exchange_code_for_token(code: str) -> dict:
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.post(
            SPOTIFY_TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": settings.spotify_redirect_uri,
            },
            auth=(settings.spotify_client_id, settings.spotify_client_secret),
        )
        response.raise_for_status()
        return response.json()
