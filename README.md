# Ouvinte Curioso API

FastAPI backend for the Ouvinte Curioso MVP.

## Stack

- Python 3.13
- FastAPI
- uv
- PostgreSQL via Docker Compose
- Spotify Web API
- pytest
- ruff

## Local Setup

```powershell
uv sync
Copy-Item .env.example .env
docker compose up -d
```

Set `APP_SECRET_KEY` and the Spotify values in `.env`:

```env
APP_SECRET_KEY=
SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=
SPOTIFY_REDIRECT_URI=http://127.0.0.1:8000/auth/spotify/callback
SPOTIFY_SCOPES=user-read-currently-playing user-read-playback-state
```

Use this redirect URI in the Spotify Developer Dashboard:

```text
http://127.0.0.1:8000/auth/spotify/callback
```

## Run

```powershell
uv run uvicorn app.main:app --reload
```

```powershell
uv run pytest
uv run ruff check .
```

## Current Routes

- `GET /health`
- `GET /auth/spotify/login`
- `GET /auth/spotify/callback`
- `POST /auth/logout`
- `GET /auth/me`
- `GET /me/player/currently-playing`

## Auth Contract

`GET /auth/me` returns:

```json
{
  "authenticated": false,
  "spotify_user": null
}
```

or:

```json
{
  "authenticated": true,
  "spotify_user": null
}
```

`spotify_user` is intentionally `null` for now.

## Docs

- [Foundation](docs/foundation/Ouvinte_Curioso_Fundacao_v1.md)
- [Backend stack decision](docs/decisions/001-backend-stack.md)
- [Spotify auth POC audit](docs/auth/spotify-auth-poc-audit.md)
- [Auth contract](docs/auth/auth-contract.md)

## Current Limitations

- Tokens are still stored inside a signed HTTP-only cookie.
- There is no server-side session persistence yet.
- There is no refresh token flow yet.
- There is no Angular frontend yet.
- There is no deploy yet.
