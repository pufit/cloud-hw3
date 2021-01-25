from abc import abstractmethod
from typing import List, Dict

import pandas as pd


class AbstractDataSource:
    @abstractmethod
    def read_data(self, *args, **kwargs) -> List[Dict]:
        """
        :return: list of dicts with the same keys
        """
        pass


class CSV(AbstractDataSource):
    def __init__(self, path):
        self._path = path

    def read_data(self, to_dict=True, **read_csv_kwargs) -> (List[Dict], pd.DataFrame):
        res = pd.read_csv(self._path, **read_csv_kwargs)
        return res.to_dict('records') if to_dict else res
