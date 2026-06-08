from pydantic import BaseModel


class TrackDto(BaseModel):
    spotify_id: str
    name: str
    artists: list[str]
    album: str
    release_date: str | None = None
    image_url: str | None = None
    spotify_url: str | None = None


class CurrentlyPlayingDto(BaseModel):
    is_playing: bool
    progress_ms: int | None = None
    track: TrackDto | None = None
