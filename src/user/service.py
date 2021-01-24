from src.common.data_source import AbstractDataSource


class UserService:
    key = 'user_id'
    data_keys = ('gender', 'age')

    def __init__(self, data_source: AbstractDataSource):
        self._data = dict()
        data = data_source.read_data()
        for row in data:
            assert row[self.key] not in self._data, f'Key value {self.key}={row[self.key]} is not unique in self._data'
            self._data[row[self.key]] = {k: row[k] for k in self.data_keys}

    def get_user_data(self, user_id):
        return self._data.get(user_id)
