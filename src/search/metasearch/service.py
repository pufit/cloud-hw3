from typing import List, Dict

from geo.service import GeoService
from search.service import BaseSearchService
from user.service import UserService


class MetaSearchService:
    def __init__(self, search: BaseSearchService, user_service: UserService, geo_service: GeoService):
        self._search = search
        self._user_service = user_service
        self._geo_service = geo_service

    def search(self, search_text, user_id, ip, limit=10) -> List[Dict]:
        user_data = self._user_service.get_user_data(user_id)  # {'gender': ..., 'age': ...}
        geo_data = self._geo_service.get_geo_data(ip)  # {'region': ...}
        df = self._search.get_search_data(search_text, user_data, geo_data, limit)
        return df[self._search.DOCS_COLUMNS].to_dict('records')
