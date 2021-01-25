from common.data_source import CSV
from geo.service import GeoService
from metasearch.http import Server
from metasearch.service import MetaSearchService
from search.service import SearchInShardsService, SimpleSearchService
from settings import USER_DATA_FILE, GEO_DATA_FILE, SEARCH_DOCUMENTS_DATA_FILES
from user.service import UserService


def main():
    user_service = UserService(CSV(USER_DATA_FILE))
    geo_service = GeoService(CSV(GEO_DATA_FILE))
    search = SearchInShardsService(shards=[SimpleSearchService(CSV(file)) for file in SEARCH_DOCUMENTS_DATA_FILES])
    metasearch = MetaSearchService(search, user_service, geo_service)
    server = Server('metasearch', metasearch=metasearch)
    server.run_server(debug=True)


if __name__ == '__main__':
    main()
