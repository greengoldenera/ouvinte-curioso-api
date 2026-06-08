from pydantic import BaseModel


class AuthMeResponse(BaseModel):
    authenticated: bool
    spotify_user: None = None
