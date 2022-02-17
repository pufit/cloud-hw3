
import aiohttp

from search.common import structures


class BaseSearchClient:
    def __init__(self, endpoint: str = 'http://localhost:8000'):
        self._endpoint = endpoint

    async def get_search_data(self, request: structures.BaseSearchRequest) -> structures.DocumentList:
        async with aiohttp.ClientSession(self._endpoint, raise_for_status=True) as session:
            async with session.post('/get_search_data', json=request.dict()) as response:
                return structures.DocumentList.parse_obj(await response.json())
