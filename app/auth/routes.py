import secrets

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse, RedirectResponse

from app.auth.schemas import AuthMeResponse
from app.auth.session import (
    create_session_cookie_value,
    delete_oauth_state_cookie,
    delete_session_cookie,
    load_session_payload,
    set_oauth_state_cookie,
    set_session_cookie,
)
from app.auth.spotify_oauth import build_authorize_url, exchange_code_for_token
from app.core.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/spotify/login")
def spotify_login() -> RedirectResponse:
    state = secrets.token_urlsafe(24)
    response = RedirectResponse(build_authorize_url(state))
    set_oauth_state_cookie(response, state)
    return response


@router.get("/spotify/callback")
async def spotify_callback(request: Request, code: str, state: str) -> JSONResponse:
    expected_state = request.cookies.get(settings.oauth_state_cookie_name)
    if not expected_state or state != expected_state:
        raise HTTPException(status_code=400, detail="Invalid OAuth state")

    token_data = await exchange_code_for_token(code)
    session_value = create_session_cookie_value(token_data)

    response = JSONResponse({"authenticated": True})
    set_session_cookie(response, session_value)
    delete_oauth_state_cookie(response)
    return response


@router.post("/logout")
def logout() -> JSONResponse:
    response = JSONResponse({"authenticated": False})
    delete_session_cookie(response)
    delete_oauth_state_cookie(response)
    return response


@router.get("/me", response_model=AuthMeResponse)
def me(request: Request) -> AuthMeResponse:
    return AuthMeResponse(authenticated=load_session_payload(request) is not None)
