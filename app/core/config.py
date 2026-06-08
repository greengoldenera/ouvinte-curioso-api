from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str
    app_secret_key: str
    frontend_url: str
    api_base_url: str
    database_url: str
    spotify_client_id: str
    spotify_client_secret: str
    spotify_redirect_uri: str
    spotify_scopes: str
    session_cookie_name: str = "oc_session"
    oauth_state_cookie_name: str = "spotify_oauth_state"
    cookie_secure: bool = False
    cookie_samesite: Literal["lax", "strict", "none"] = "lax"
    session_cookie_max_age_seconds: int = 604800
    oauth_state_cookie_max_age_seconds: int = 600

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
