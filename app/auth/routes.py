import secrets

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse, RedirectResponse
from itsdangerous import BadSignature, URLSafeSerializer

from app.auth.spotify_oauth import build_authorize_url, exchange_code_for_token
from app.core.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])
serializer = URLSafeSerializer(settings.app_secret_key, salt="spotify-session")


@router.get("/spotify/login")
def spotify_login() -> RedirectResponse:
    state = secrets.token_urlsafe(24)
    response = RedirectResponse(build_authorize_url(state))
    response.set_cookie(
        key=settings.oauth_state_cookie_name,
        value=state,
        httponly=True,
        secure=settings.cookie_secure,
        samesite=settings.cookie_samesite,
        max_age=settings.oauth_state_cookie_max_age_seconds,
    )
    return response


@router.get("/spotify/callback")
async def spotify_callback(request: Request, code: str, state: str) -> JSONResponse:
    expected_state = request.cookies.get(settings.oauth_state_cookie_name)
    if not expected_state or state != expected_state:
        raise HTTPException(status_code=400, detail="Invalid OAuth state")

    token_data = await exchange_code_for_token(code)
    session_value = serializer.dumps(
        {
            "access_token": token_data["access_token"],
            "refresh_token": token_data.get("refresh_token"),
            "expires_in": token_data.get("expires_in"),
        }
    )

    response = JSONResponse({"authenticated": True})
    response.set_cookie(
        key=settings.session_cookie_name,
        value=session_value,
        httponly=True,
        secure=settings.cookie_secure,
        samesite=settings.cookie_samesite,
        max_age=settings.session_cookie_max_age_seconds,
    )
    response.delete_cookie(
        settings.oauth_state_cookie_name,
        secure=settings.cookie_secure,
        samesite=settings.cookie_samesite,
    )
    return response


@router.post("/logout")
def logout() -> JSONResponse:
    response = JSONResponse({"authenticated": False})
    response.delete_cookie(
        settings.session_cookie_name,
        secure=settings.cookie_secure,
        samesite=settings.cookie_samesite,
    )
    return response


@router.get("/me")
def me(request: Request) -> dict[str, bool]:
    session_cookie = request.cookies.get(settings.session_cookie_name)
    if not session_cookie:
        return {"authenticated": False}

    try:
        serializer.loads(session_cookie)
    except BadSignature:
        return {"authenticated": False}

    return {"authenticated": True}
