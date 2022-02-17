import os

from search.common.utils import Singleton


class UsersServiceConfig:
    data_path = os.getenv('USERS_DATA_PATH', 'data/users.csv')


class BaseSearchConfig:
    data_path = os.getenv('BASE_SEARCH_DATA_PATH', 'data/news_generated.csv')


class IntSearchConfig:
    base_search_endpoints = os.getenv('INT_BASE_SEARCH_ENDPOINTS', 'http://localhost:8000').split(',')


class MetaSearchConfig:
    int_search_endpoint = os.getenv('META_INT_SEARCH_ENDPOINTS', 'http://localhost:8100')
    users_service_endpoint = os.getenv('META_USERS_ENDPOINTS', 'http://localhost:7999')


class Config(metaclass=Singleton):
    users_service_config = UsersServiceConfig()

    basesearch_config = BaseSearchConfig()

    intsearch_config = IntSearchConfig()

    metasearch_config = MetaSearchConfig()
