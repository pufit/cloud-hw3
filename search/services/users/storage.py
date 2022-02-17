import typing as tp

from search.common.data_source import AbstractDataSource


class UserStorage:
    key = 'user_id'
    data_keys = ('user_id', 'gender', 'age')

    def __init__(self, data_source: AbstractDataSource):
        self._data: tp.Dict[int, tp.Dict] = {}

        data = data_source.read_data()

        for row in data:
            if row[self.key] in self._data:
                raise ValueError(f'Key value {self.key}={row[self.key]} is not unique')

            self._data[row[self.key]] = {k: row[k] for k in self.data_keys}

    def get(self, user_id: int) -> tp.Dict:
        return self._data.get(user_id)
