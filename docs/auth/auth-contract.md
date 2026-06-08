# Auth Contract

Status: Current frontend integration contract

## Purpose

This document defines the current auth contract for frontend integration.

## Current Auth Flow

1. Frontend opens `GET /auth/spotify/login`.
2. Backend redirects to Spotify authorization.
3. Spotify redirects to `GET /auth/spotify/callback`.
4. Backend validates OAuth `state`.
5. Backend sets a signed HTTP-only session cookie.
6. Backend returns `{"authenticated": true}`.

## Cookies

- `SESSION_COOKIE_NAME`
  - Default: `oc_session`
  - Stores the signed backend session value.

- `OAUTH_STATE_COOKIE_NAME`
  - Default: `spotify_oauth_state`
  - Stores the temporary OAuth state value.

Current cookie behavior:

- cookies are HTTP-only;
- `secure` is configurable;
- `sameSite` is configurable;
- max age is configurable;
- tokens are not returned to frontend JSON.

## GET /auth/me

Unauthenticated response:

```json
{
  "authenticated": false,
  "spotify_user": null
}
```

Authenticated response:

```json
{
  "authenticated": true,
  "spotify_user": null
}
```

`spotify_user` is intentionally `null` for now. It is reserved for a future server-side persisted Spotify user profile.

## POST /auth/logout

Response:

```json
{
  "authenticated": false
}
```

Behavior:

- deletes the session cookie;
- deletes the OAuth state cookie.

## Related Auth-Dependent Route

- `GET /me/player/currently-playing`
  - Depends on the auth session cookie.
  - It is not part of the auth contract details in this document.

## Current Limitations

- Tokens are still inside the signed cookie.
- There is no server-side session persistence yet.
- There is no refresh token flow yet.
- There is no Spotify `/me` profile call yet.

## Non-Goals

- No frontend implementation.
- No deploy.
- No Redis.
- No Google login.
- No complex auth architecture.
