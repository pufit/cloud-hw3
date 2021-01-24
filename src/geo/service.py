import ipaddress as ip

import pandas as pd

from src.common.data_source import CSV


class GeoService:
    _data: pd.DataFrame
    _networks: pd.Series

    def __init__(self, data_source: CSV):
        self._data = data_source.read_data(to_dict=False)
        for col in ('network', 'country_name'):
            assert col in self._data.columns
        self._networks = self._data['network'].apply(ip.ip_network)

    def get_geo_data(self, ip_addr):
        try:
            addr = ip.ip_address(ip_addr)
        except ValueError:
            return None
        addr_in_net = self._networks.apply(lambda x: addr in x)
        addr_in_net = addr_in_net[addr_in_net == True]
        if len(addr_in_net) > 0:
            return {'region': self._data.loc[addr_in_net.head(1).index].iloc[0].country_name}
        return None
