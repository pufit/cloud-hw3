import os

BASE_DIR = os.sep.join(os.path.normpath(__file__).split(os.sep)[:-3])
BASE_DATA_DIR = os.path.join(BASE_DIR, 'data')
assert os.path.exists(BASE_DATA_DIR)


def datafile(file):
    return os.path.join(BASE_DATA_DIR, file)


USER_DATA_FILE = datafile('users.csv')
GEO_DATA_FILE = datafile('geo.csv')
SEARCH_DOCUMENTS_DATA_FILES = [datafile(f'news_generated.{i}.csv') for i in range(1, 4)]
