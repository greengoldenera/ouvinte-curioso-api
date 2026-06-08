from collections.abc import Mapping
from typing import Any

from fastapi import HTTPException, Request
from itsdangerous import BadSignature, URLSafeSerializer

from app.core.config import settings

session_serializer = URLSafeSerializer(settings.app_secret_key, salt="spotify-session")


def create_session_cookie_value(token_data: Mapping[str, Any]) -> str:
    return session_serializer.dumps(
        {
            "access_token": token_data["access_token"],
            "refresh_token": token_data.get("refresh_token"),
            "expires_in": token_data.get("expires_in"),
        }
    )


def load_session_payload(request: Request) -> dict[str, Any] | None:
    session_cookie = request.cookies.get(settings.session_cookie_name)
    if not session_cookie:
        return None

    try:
        return session_serializer.loads(session_cookie)
    except BadSignature:
        return None


def require_session_tokens(request: Request) -> dict[str, Any]:
    session_cookie = request.cookies.get(settings.session_cookie_name)
    if not session_cookie:
        raise HTTPException(status_code=401, detail="Not authenticated")

    try:
        return session_serializer.loads(session_cookie)
    except BadSignature as exc:
        raise HTTPException(status_code=401, detail="Invalid session") from exc
