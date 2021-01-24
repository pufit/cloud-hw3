import pytest
import pandas as pd

from src.common.data_source import AbstractDataSource
from src.geo.service import GeoService


@pytest.fixture
def data_source():
    class SomeDataSource(AbstractDataSource):
        def read_data(self, *args, **kwargs):
            return pd.DataFrame([{'network': '192.168.1.0/24', 'country_name': 'Some Country'}])
    return SomeDataSource()


def test_geo_service(data_source):
    service = GeoService(data_source)
    assert service.get_geo_data('192.168.1.255') == {'region': 'Some Country'}
    assert service.get_geo_data('192.168.0.1') is None
    assert service.get_geo_data('abc') is None
