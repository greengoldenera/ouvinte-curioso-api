# Spotify Auth POC Audit

Status: Current POC state

## Scope

This document describes the current Spotify authentication POC based on:

- `app/main.py`
- `app/core/config.py`
- `app/auth/routes.py`
- `app/auth/spotify_oauth.py`
- `app/spotify/routes.py`
- `app/tests/test_auth_security.py`

Application code was not changed for this audit.

## Current Implemented Routes

- `GET /auth/spotify/login`
  - Creates an OAuth `state`.
  - Redirects to Spotify authorization.
  - Stores `spotify_oauth_state` in an HTTP-only cookie.

- `GET /auth/spotify/callback`
  - Validates the returned OAuth `state`.
  - Exchanges the authorization code for Spotify tokens.
  - Stores `access_token`, `refresh_token`, and `expires_in` in a signed `oc_session` cookie.
  - Returns `{"authenticated": true}`.

- `POST /auth/logout`
  - Deletes the `oc_session` cookie.
  - Returns `{"authenticated": false}`.

- `GET /auth/me`
  - Reads and validates the signed `oc_session` cookie.
  - Returns only `{"authenticated": true}` or `{"authenticated": false}`.

- `GET /me/player/currently-playing`
  - Requires a valid `oc_session` cookie.
  - Uses the stored Spotify access token to call Spotify currently-playing.
  - Returns a clean `CurrentlyPlayingDto`.

## Current Strengths

- Spotify OAuth is working end to end in the backend POC.
- OAuth `state` validation exists before token exchange.
- Tokens are not returned in JSON responses.
- The `oc_session` cookie is HTTP-only.
- Basic auth security tests exist:
  - currently-playing requires authentication;
  - `/auth/me` does not expose access or refresh tokens.

## Current MVP Gaps

- `access_token` and `refresh_token` are stored inside the signed cookie.
- There is no server-side session persistence yet.
- There is no refresh token flow yet.
- Cookie settings such as `secure`, `max_age`, and `samesite` are not centralized or configurable.
- `/auth/me` returns only an `authenticated` boolean.
- The database session exists but is not used by auth yet.

## Recommended Next Steps

1. Harden settings and cookie configuration.
2. Organize the auth module if needed as the flow grows.
3. Define the `/auth/me` contract needed by the future frontend.
4. Move Spotify tokens to server-side persistence.
5. Implement refresh token support later, after session persistence is in place.

## Explicit Non-Goals For Now

- No frontend implementation.
- No deploy work.
- No Redis.
- No Google login.
- No complex auth architecture.
