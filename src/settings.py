import os

BASE_DIR = os.sep.join(os.path.normpath(__file__).split(os.sep)[:-2])
BASE_DATA_DIR = os.path.join(BASE_DIR, 'data')
assert os.path.exists(BASE_DATA_DIR)


def datafile(file):
    return os.path.join(BASE_DATA_DIR, file)


USER_DATA_FILE = datafile('users.csv')
GEO_DATA_FILE = datafile('geo.csv')
REQUESTS_DATA_FILE = ''
SEARCH_DOCUMENTS_DATA_FILES = [datafile(f'news_shard_{i}.csv') for i in range(1, 4)]
