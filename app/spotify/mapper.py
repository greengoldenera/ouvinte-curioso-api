from app.spotify.schemas import CurrentlyPlayingDto, TrackDto


def map_currently_playing_payload(payload: dict) -> CurrentlyPlayingDto:
    item = payload.get("item")

    if not item:
        return CurrentlyPlayingDto(
            is_playing=False,
            progress_ms=None,
            track=None,
        )

    images = item.get("album", {}).get("images", [])
    image_url = images[0]["url"] if images else None

    return CurrentlyPlayingDto(
        is_playing=bool(payload.get("is_playing")),
        progress_ms=payload.get("progress_ms"),
        track=TrackDto(
            spotify_id=item["id"],
            name=item["name"],
            artists=[
                artist["name"]
                for artist in item.get("artists", [])
            ],
            album=item.get("album", {}).get("name", ""),
            release_date=item.get("album", {}).get("release_date"),
            image_url=image_url,
            spotify_url=item.get("external_urls", {}).get("spotify"),
        ),
    )
