import numpy as np
import pandas as pd
import pytest

from src.common.data_source import AbstractDataSource
from src.search.service import SimpleSearchService, SearchInShardsService


@pytest.fixture
def data_source():
    class SomeDataSource(AbstractDataSource):
        def read_data(self):
            return [{'document': 'some document', 'key': 'some_key', 'gender': 'male,female',
                     'age_from': 0, 'age_to': 10, 'region': 'Some Region'},
                    {'document': 'another document', 'key': 'another_key', 'gender': 'female',
                     'age_from': 15, 'age_to': 30, 'region': 'Another Region'},
                    {'document': 'some another document', 'key': 'some_another_key', 'gender': 'male',
                     'age_from': 20, 'age_to': 25, 'region': 'Some Region'}]

    return SomeDataSource()


@pytest.fixture
def search_service(data_source):
    return SimpleSearchService(data_source)


def test_build_tokens_count(search_service):
    res = search_service._build_tokens_count('some another')
    assert all(res == pd.Series([1, 1, 2]))


def test_get_geo_mask(search_service):
    res = search_service._get_geo_mask(geo_data={'region': 'Some Region'})
    assert all(res == pd.Series([True, False, True]))


def test_get_gender_mask(search_service):
    res = search_service._get_gender_mask(user_data={'gender': 'female'})
    assert all(res == pd.Series([True, True, False]))


def test_get_age_mask(search_service):
    res = search_service._get_age_mask(user_data={'age': '21'})
    assert all(res == pd.Series([False, True, True]))


def test_get_search_data(search_service):
    res = search_service.get_search_data(
        'some another',
        user_data={'gender': 'female', 'age': '21'},
        geo_data={'region': 'Some Region'},
        limit=2
    )
    expected = pd.Series(['some_another_key', 'some_key'])
    assert np.array_equal(res.key, expected)


def test_search_in_shards():
    class SomeDataSource(AbstractDataSource):
        def __init__(self, rows):
            self._rows = rows

        def read_data(self):
            return self._rows

    ds1 = SomeDataSource([{'document': 'some document', 'key': 'some_key', 'gender': 'male,female',
                           'age_from': 0, 'age_to': 10, 'region': 'Some Region'}])
    ds2 = SomeDataSource([{'document': 'another document', 'key': 'another_key', 'gender': 'female',
                           'age_from': 15, 'age_to': 30, 'region': 'Another Region'},
                          {'document': 'some another document', 'key': 'some_another_key', 'gender': 'male',
                           'age_from': 20, 'age_to': 25, 'region': 'Some Region'}])
    shard1 = SimpleSearchService(ds1)
    shard2 = SimpleSearchService(ds2)
    search_service = SearchInShardsService([shard1, shard2])
    res = search_service.get_search_data(
        'some another',
        user_data={'gender': 'female', 'age': '21'},
        geo_data={'region': 'Some Region'},
        limit=2
    )
    expected = pd.Series(['some_another_key', 'some_key'])
    assert np.array_equal(res.key, expected)
