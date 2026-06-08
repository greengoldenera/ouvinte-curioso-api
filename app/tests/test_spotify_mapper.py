from app.spotify.mapper import map_currently_playing_payload


def test_map_currently_playing_payload_with_track() -> None:
    payload = {
        "is_playing": True,
        "progress_ms": 42000,
        "item": {
            "id": "track-123",
            "name": "Test Song",
            "artists": [{"name": "Artist One"}, {"name": "Artist Two"}],
            "album": {
                "name": "Test Album",
                "release_date": "2026-06-08",
                "images": [{"url": "https://example.com/image.jpg"}],
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/track-123",
            },
        },
    }

    result = map_currently_playing_payload(payload)

    assert result.is_playing is True
    assert result.progress_ms == 42000
    assert result.track is not None
    assert result.track.spotify_id == "track-123"
    assert result.track.name == "Test Song"
    assert result.track.artists == ["Artist One", "Artist Two"]
    assert result.track.album == "Test Album"
    assert result.track.release_date == "2026-06-08"
    assert result.track.image_url == "https://example.com/image.jpg"
    assert result.track.spotify_url == "https://open.spotify.com/track/track-123"


def test_map_currently_playing_payload_without_track() -> None:
    result = map_currently_playing_payload({"is_playing": False})

    assert result.is_playing is False
    assert result.progress_ms is None
    assert result.track is None
