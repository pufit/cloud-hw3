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
    params = 'text=United&user_id=35&ip_addr=4.18.64.10'
    url = f'{search_baseurl}/{path}?{params}'
    response = requests.get(url)
    expected = {
        "search_results": [
            {
                "document": "  Soliman S. Biheiri, the only person convicted in a broad probe into whether Islamic charities in Northern Virginia were financing terrorist organizations, pleaded guilty yesterday to illegally possessing and using a U.S. passport to enter the United States last year.",
                "key": "Man Pleads Guilty in Passport Case",
                "key_md5": "f69e5df07d9f19f865dd2c0656950c76"
            },
            {
                "document": "SEOUL - The head of the United Nations #39; nuclear watchdog, Mr Mohamed El-Baradei, arrived in Seoul yesterday to discuss South Korea #39;s nuclear experiments.",
                "key": "IAEA head in Seoul to discuss nuclear activities",
                "key_md5": "edaa3a51f2d8cfbcaa774b922359d346"
            },
            {
                "document": "UNITED NATIONS, New York For years, Kofi Annan was seen at the United Nations as a Mandela-like figure, a statesman who brought a serene sense of personal confidence and institutional steadiness to the task of settling conflict and a person frequently ",
                "key": "Annan is teetering on his pedestal",
                "key_md5": "b30c5ef504b8b190d5be787284223e58"
            },
            {
                "document": " WASHINGTON (Reuters) - The United States hopes to boost the  availability of electricity throughout Iraq to at least 18  hours a day by the end of next year from 11 to 15 hours now,  the top U.S. aid official said on Friday.",
                "key": "U.S. Aims to Boost Electricity in Iraq to 20 Hours",
                "key_md5": "a249e2ce2386a60758c8030e18074f1f"
            },
            {
                "document": "A couple of years ago Sheikh Zayed ibn Sultan Al-Nahyan, the emir of Abu Dhabi and president of the United Arab Emirates (UAE) patronized the translation and publication of an old Islamic text about the ideal prince.",
                "key": "Editorial: The Ideal Prince",
                "key_md5": "971e682dc26433bb5a2e6fea9dd0728a"
            },
            {
                "document": "Canadian Press - KHARTOUM, Sudan (CP) - Sudan isn't afraid of a U.S.-backed United Nations resolution threatening sanctions over the violence in Darfur, President Omar el-Bashir was quoted as saying Sunday.",
                "key": "Sudan says it's not afraid of UN resolution threatening sanctions (Canadian Press)",
                "key_md5": "8076a967528e5ec5982bd26ec4cadde6"
            },
            {
                "document": "USATODAY.com - President Bush says U.S. forces will stay in Iraq as long as necessary but no longer. John Kerry says he wants to bring U.S. troops home but will not \"cut and run\" before the country is stable. Despite differences over how the United States went to war, either man as president would pursue a similar strategy now, their campaign statements show.",
                "key": "Bush, Kerry have similar postwar strategies (USATODAY.com)",
                "key_md5": "7bc560589f9652de20a8ed3edbbddd94"
            },
            {
              "document": " KABUL (Reuters) - The United States has brokered a  cease-fire between a renegade Afghan militia leader and the  embattled governor of the western province of Herat,  Washington's envoy to Kabul said Tuesday.  \"Our expectation is that the agreement that has been made will  be honored,\" said ambassador Zalmay Khalilzad, adding that the  cease-fire was due to take effect at 4 p.m.",
              "key": "U.S. Brokers Cease-fire in Western Afghanistan",
              "key_md5": "6da7b77e00df9731a8f34c84d29da5e0"
            },
            {
                "document": "Approximately 500 D.C. United fans gathered at RFK Stadium on Tuesday to celebrate the team's victory in Sunday's MLS Cup.",
                "key": "Fans Honor United",
                "key_md5": "6be72bd14ef8ea256db05ec6ff792372"
            },
            {
                "document": "A PRIEST accused of bulldozing more than 2000 Tutsi villagers to death as they sought sanctuary in his church during Rwanda #39;s 1994 genocide has gone on trial before a United Nations court charged with crimes against humanity.",
                "key": "Priest on trial over killing of 2000 Rwandans",
                "key_md5": "62bfbbe99edebcfecff77b08bcfab415"
            }
        ]
    }
    assert response.json() == expected
