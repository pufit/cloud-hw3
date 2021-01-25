import pytest

from common.data_source import CSV
from geo.service import GeoService
from metasearch.service import MetaSearchService
from search.service import SearchInShardsService, SimpleSearchService
from settings import USER_DATA_FILE, GEO_DATA_FILE, SEARCH_DOCUMENTS_DATA_FILES
from user.service import UserService


@pytest.fixture
def metasearch():
    user_service = UserService(CSV(USER_DATA_FILE))
    geo_service = GeoService(CSV(GEO_DATA_FILE))
    search = SearchInShardsService(shards=[SimpleSearchService(CSV(file)) for file in SEARCH_DOCUMENTS_DATA_FILES])
    return MetaSearchService(search, user_service, geo_service)


def test_integration_works(metasearch):
    res = metasearch.search(search_text='politician', user_id=25, ip='3.103.8.10', limit=5)
    result_keys = [d['key'] for d in res]
    expected_keys = [
        'Dutch crackdown risks hurting mainstream Muslims',
        'Dutch Filmmaker Murder Suspect Faces Terror Charges',
        'Surprise victory for Basescu in Romania',
        'BLAIR PEACE HOPES',
        'France Opens Judicial Inquiry Into Holocaust Doubter'
    ]
    assert result_keys == expected_keys


def test_integration_bad_parameters(metasearch):
    metasearch.search(search_text='politician', user_id=None, ip='0.0.0.0', limit=10)
    metasearch.search(search_text='politician', user_id=None, ip=None, limit=1)
    metasearch.search(search_text=None, user_id=None, ip=None, limit=1)
    metasearch.search(search_text='', user_id=None, ip=None, limit=1)
