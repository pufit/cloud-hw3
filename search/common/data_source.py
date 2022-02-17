import typing as tp

import pandas as pd


class AbstractDataSource:
    def read_data(self, *args, **kwargs) -> tp.List[tp.Dict]:
        raise NotImplementedError()


class CSV(AbstractDataSource):
    def __init__(self, path):
        self._path = path

    def read_data(self, to_dict=True, **read_csv_kwargs) -> tp.Union[tp.List[tp.Dict], pd.DataFrame]:
        res = pd.read_csv(self._path, **read_csv_kwargs)
        return res.to_dict('records') if to_dict else res
