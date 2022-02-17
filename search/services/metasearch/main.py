from fastapi import FastAPI

from search.common import structures
from search.common.config import Config
from search.services.basesearch.client import BaseSearchClient
from search.services.users.client import UsersClient


app = FastAPI()

config = Config()

int_search_client: BaseSearchClient = BaseSearchClient(config.metasearch_config.int_search_endpoint)

users_client = UsersClient(config.metasearch_config.users_service_endpoint)


@app.get('/search', response_model=structures.SearchResult)
async def search(text: str, user_id: int, limit: int = 10):
    user_data = await users_client.get_user(user_id)

    result = await int_search_client.get_search_data(structures.BaseSearchRequest(
        search_text=text,
        user_data=user_data,
        limit=limit
    ))

    return result.dict()
