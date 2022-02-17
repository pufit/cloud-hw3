
import aiohttp

from search.common import structures


class UsersClient:
    def __init__(self, endpoint: str = 'http://localhost:7999'):
        self._endpoint = endpoint

    async def get_user(self, user_id: int) -> structures.User:
        async with aiohttp.ClientSession(self._endpoint, raise_for_status=True) as session:
            async with session.get(f'/users/{user_id}') as response:
                return structures.User.parse_obj(await response.json())
