from typing import List, Dict

from search.service import BaseSearchService
from user.service import UserService


class MetaSearchService:
    def __init__(self, search: BaseSearchService, user_service: UserService) -> None:
        self._search = search
        self._user_service = user_service

    def search(self, search_text, user_id, limit=10) -> List[Dict]:
        user_data = self._user_service.get_user_data(user_id)  # {'gender': ..., 'age': ...}
        df = self._search.get_search_data(search_text, user_data, limit)
        return df[self._search.DOCS_COLUMNS].to_dict('records')
