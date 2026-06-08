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
