# Ouvinte Curioso API

POC backend para validar FastAPI + Spotify OAuth + currently-playing.

## Stack

- Python
- FastAPI
- uv
- PostgreSQL via Docker Compose
- pytest
- ruff
- Spotify Web API

## Setup local

`powershell
uv sync
Copy-Item .env.example .env
docker compose up -d
`

Preencha no .env:

`env
APP_SECRET_KEY=
SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=
`

Redirect URI no Spotify Developer Dashboard:

`	ext
http://127.0.0.1:8000/auth/spotify/callback
`

## Rodar API

`powershell
uv run uvicorn app.main:app --reload
`

URLs:

`	ext
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/auth/spotify/login
http://127.0.0.1:8000/me/player/currently-playing
`

## Testes e lint

`powershell
uv run pytest
uv run ruff check .
`

## Escopo da POC

Inclui:

* OAuth Spotify;
* sessão server-side simplificada;
* consulta de música atual;
* DTO limpo para frontend;
* testes básicos.

Não inclui:

* frontend Angular;
* IA;
* letras;
* deploy;
* refresh token persistente;
* banco modelado.

## Limitação conhecida

O refresh token ainda não foi persistido em banco. Para a POC, a sessão usa cookie assinado.
