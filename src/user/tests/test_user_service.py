import pytest

from src.common.data_source import AbstractDataSource
from src.user.service import UserService


@pytest.fixture
def data_source():
    class SomeDataSource(AbstractDataSource):
        def read_data(self):
            return [{'user_id': 1, 'gender': 'male', 'age': 12},
                    {'user_id': 2, 'gender': 'female', 'age': 25}]
    return SomeDataSource()


def test_user_service(data_source):
    service = UserService(data_source)
    assert service.get_user_data(1) == {'gender': 'male', 'age': 12}
    assert service.get_user_data(0) is None
