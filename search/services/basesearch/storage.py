import pandas as pd

from search.common.data_source import AbstractDataSource


class BaseSearchStorage(pd.DataFrame):

    COLUMNS = ['document', 'key', 'key_md5', 'gender', 'age_from', 'age_to', 'region']

    def __init__(self, data_source: AbstractDataSource):
        super().__init__(
            data_source.read_data(),
            columns=self.COLUMNS
        )
