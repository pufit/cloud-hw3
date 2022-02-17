from fastapi import FastAPI
import asyncio
import typing as tp
import pandas as pd

from search.common import structures
from search.common.config import Config
from search.services.basesearch.client import BaseSearchClient
from search.services.basesearch.range    import range_sort

app = FastAPI()

config = Config()

clients: tp.List[BaseSearchClient] = [BaseSearchClient(endpoint) for endpoint in config.intsearch_config.base_search_endpoints]


@app.post('/get_search_data', response_model=structures.DocumentList)
async def get_search_data(request: structures.BaseSearchRequest):
    shards_responses = await asyncio.gather(*(
        shard.get_search_data(request)
        for shard in clients
    ))

    data_frames: tp.List[pd.DataFrame] = []

    for response in shards_responses:
        if not isinstance(response, BaseException):
            data_frames.append(pd.DataFrame(
                response.dict()['documents']
            ))

    data = pd.concat(data_frames)
    data.drop_duplicates(inplace=True)
    data.reset_index(inplace=True, drop=True)

    assert data.index.is_unique
    return range_sort(data, request)
