from fastapi.testclient import TestClient

from app.auth.session import session_serializer
from app.core.config import settings
from app.main import app


client = TestClient(app)


def test_currently_playing_requires_auth() -> None:
    response = client.get("/me/player/currently-playing")

    assert response.status_code == 401


def test_me_does_not_return_tokens() -> None:
    session = session_serializer.dumps(
        {
            "access_token": "secret-access",
            "refresh_token": "secret-refresh",
        }
    )

    response = client.get(
        "/auth/me",
        cookies={settings.session_cookie_name: session},
    )

    assert response.status_code == 200
    assert response.json() == {"authenticated": True}
    assert "access_token" not in response.text
    assert "refresh_token" not in response.text


def test_logout_deletes_auth_cookies() -> None:
    response = client.post("/auth/logout")

    set_cookie_headers = response.headers.get_list("set-cookie")

    assert response.status_code == 200
    assert response.json() == {"authenticated": False}
    assert any(
        header.startswith(f"{settings.session_cookie_name}=")
        and "Max-Age=0" in header
        for header in set_cookie_headers
    )
    assert any(
        header.startswith(f"{settings.oauth_state_cookie_name}=")
        and "Max-Age=0" in header
        for header in set_cookie_headers
    )
