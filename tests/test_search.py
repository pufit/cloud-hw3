import time

import pytest
import requests

from settings import SEARCH_SERVICE_ADDRESS, SEARCH_SERVICE_PORT


@pytest.fixture
def search_baseurl():
    return f'http://{SEARCH_SERVICE_ADDRESS}:{SEARCH_SERVICE_PORT}'


@pytest.fixture
def ensure_search_running(search_baseurl):
    while True:
        try:
            response = requests.get(search_baseurl)
            assert response.status_code == 404
            break
        except requests.exceptions.ConnectionError:
            print('Waiting for search to run...')
            time.sleep(1)


@pytest.mark.usefixtures('ensure_search_running')
def test_search_service(search_baseurl):
    path = 'search'
    params = 'text=United&user_id=35'
    url = f'{search_baseurl}/{path}?{params}'
    response = requests.get(url)
    expected = {
        "documents": [
            {
              "document": " VALKENBURG, Netherlands (Reuters) - The European Union will  draw up sanctions against Sudan, with a view to implementing  them if the United Nations calls for such measures, the Dutch  foreign minister said on Saturday.",
              "key": "EU to Draft Sanctions Against Sudan",
              "key_md5": "fff953b12941a60769cd6533a6e89f36"
            },
            {
              "document": "AP - The U.N. Security Council voted unanimously Tuesday to hold a rare meeting in Nairobi next month to promote a peace agreement between the Sudanese government and southern rebels that the United States says also is crucial to ending the conflict in the Darfur region.",
              "key": "Security Council Votes for Nairobi Meeting (AP)",
              "key_md5": "ffe162962ad2abfd2c4fabfba82b2fb0"
            },
            {
              "document": "Zenit St. Petersburg faces the daunting prospect of being picked to play against Lazio, Newcastle United or Feyenoord in Tuesday #39;s draw for the inaugural group stage of the UEFA Cup.",
              "key": "Zenit Eyes Lazio, Newcastle in Draw",
              "key_md5": "ffda40b56e51716dd0a093082e44c6b5"
            },
            {
              "document": "Ryan Giggs will try to tie Manchester United team mate Gary Neville in knots and score a goal to send the Old Trafford crowd home in tears when Wales side play England on Saturday.",
              "key": "Giggs out to break Old Trafford hearts",
              "key_md5": "ffb166965287421f151aa614110afc16"
            },
            {
              "document": "There are plenty of reports on the final day of the Expos, how the city that no one in the United States felt deserved a team is finally losing it.",
              "key": "Top 10 depressing things about Expos #39; finale",
              "key_md5": "ff9923974df967da12c117876f60f293"
            },
            {
              "document": "Teenager Rafael Nadal led Spain into the Davis Cup final on Sunday, but then admitted he may face a bit-part role in December #39;s title clash with the United States.",
              "key": "Spain through to Davis Cup final",
              "key_md5": "ff87873e5b3c32c96359d8fcbab1087e"
            },
            {
              "document": "After 12 years of failure it is time for Taiwan to adopt a new strategy in its quest to gain a seat at the United Nations, Minister of Foreign Affairs Mark Chen () said yesterday.",
              "key": "UN under fire for rejecting the voice of Taiwan",
              "key_md5": "ff83d0b23a814c4def4b8a9fe7b8f9b9"
            },
            {
              "document": "FARMINGTON, United States : Vijay Singh shot a three-under par 69 to win the 4.2 million dollar PGA event and capture his eighth title of 2004.",
              "key": "Golf: Singh fires final round 69 to win third straight event",
              "key_md5": "ff02e1fbd5edb2a229459d0cdc7e3c99"
            },
            {
              "document": " UNITED NATIONS/KHARTOUM, Sudan (Reuters) - The United  States piled pressure on Sudan Wednesday to accept a more  powerful monitoring force in Darfur with a new U.N. draft  resolution threatening sanctions on its oil industry.",
              "key": "U.S. Piles Pressure on Sudan with New U.N. Measure",
              "key_md5": "fef86049a8a0e22a4d0606b9c967d137"
            },
            {
              "document": "D.C. United beats the MetroStars, 3-2, Sunday night in a tuneup for their first-round playoff series.",
              "key": "United Win in Season Finale",
              "key_md5": "fef81ce411b1ea8d71ed993ef0aa5a86"
            }
        ]
    }
    assert response.json() == expected
