from src.common.data_source import CSV
from src.geo.service import GeoService
from src.metasearch.http import Server
from src.metasearch.service import MetaSearchService
from src.search.service import SearchInShardsService, SimpleSearchService
from src.settings import USER_DATA_FILE, GEO_DATA_FILE, SEARCH_DOCUMENTS_DATA_FILES
from src.user.service import UserService


def main():
    user_service = UserService(CSV(USER_DATA_FILE))
    geo_service = GeoService(CSV(GEO_DATA_FILE))
    search = SearchInShardsService(shards=[SimpleSearchService(CSV(file)) for file in SEARCH_DOCUMENTS_DATA_FILES])
    metasearch = MetaSearchService(search, user_service, geo_service)
    server = Server('metasearch', metasearch=metasearch)
    server.run_server()


if __name__ == '__main__':
    main()
