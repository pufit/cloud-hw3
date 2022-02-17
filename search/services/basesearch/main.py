from fastapi import FastAPI

from search.common import structures
from search.common.config import Config
from search.common.data_source import CSV
from search.services.basesearch.storage import BaseSearchStorage
from search.services.basesearch.range import range_sort


app = FastAPI()

config = Config()

storage = BaseSearchStorage(CSV(config.basesearch_config.data_path))


@app.post('/get_search_data', response_model=structures.DocumentList)
def get_search_data(request: structures.BaseSearchRequest):
    if not request.search_text:
        return structures.DocumentList()

    return range_sort(storage, request)
