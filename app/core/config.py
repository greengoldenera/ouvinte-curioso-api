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

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
