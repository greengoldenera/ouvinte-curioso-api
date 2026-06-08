import httpx


CURRENTLY_PLAYING_URL = (
    "https://api.spotify.com/v1/me/player/currently-playing"
)


async def get_currently_playing(access_token: str) -> httpx.Response:
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(
            CURRENTLY_PLAYING_URL,
            headers={
                "Authorization": f"Bearer {access_token}",
            },
        )

        return response
