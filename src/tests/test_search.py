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
        'search_results': [
            {
                'document': 'washingtonpost.com - The Bush-Cheney reelection campaign has barred people outside the United States from viewing its Web site following an electronic attack that took down the campaign\'s Internet address for six hours last week, according\\\\to computer security experts.',
                'key': 'Bush Web Site Bars Overseas Visitors (washingtonpost.com)',
                'key_md5': 'fb82642bf871d731eb2375e959dbb09a'
            },
            {
                'document': '  Soliman S. Biheiri, the only person convicted in a broad probe into whether Islamic charities in Northern Virginia were financing terrorist organizations, pleaded guilty yesterday to illegally possessing and using a U.S. passport to enter the United States last year.',
                'key': 'Man Pleads Guilty in Passport Case',
                'key_md5': 'f69e5df07d9f19f865dd2c0656950c76'
            },
            {
                'document': 'SEOUL - The head of the United Nations #39; nuclear watchdog, Mr Mohamed El-Baradei, arrived in Seoul yesterday to discuss South Korea #39;s nuclear experiments.',
                'key': 'IAEA head in Seoul to discuss nuclear activities',
                'key_md5': 'edaa3a51f2d8cfbcaa774b922359d346'
            },
            {
                'document': ' LONDON (Reuters) - The dollar fell to a one-month low  against the yen and held near a recent one-week low versus the  euro on Monday after weak U.S. jobs data raised questions about  future interest rate hikes in the United States.',
                'key': 'Weak Jobs Growth Drags Down Dollar',
                'key_md5': 'c0afddbe0b6bbbc374c7ec88a219af1d'
            },
            {
                'document': 'UNITED NATIONS, New York For years, Kofi Annan was seen at the United Nations as a Mandela-like figure, a statesman who brought a serene sense of personal confidence and institutional steadiness to the task of settling conflict and a person frequently ',
                'key': 'Annan is teetering on his pedestal',
                'key_md5': 'b30c5ef504b8b190d5be787284223e58'
            },
            {
                'document': 'By Alistair Osborne, Associate City Editor (Filed: 17/12/2004). United Technologies Corporation clinched the acquisition of Kidde yesterday after sweetening its 165p-a-share offer for the fire protection group with a final dividend of 2p per share.',
                'key': 'Kidde succumbs to 17m  #39;sweetener #39;',
                'key_md5': 'b0b345d677cdd874cb63cdd52d68b7af'
            },
            {
                'document': ' WASHINGTON (Reuters) - The United States hopes to boost the  availability of electricity throughout Iraq to at least 18  hours a day by the end of next year from 11 to 15 hours now,  the top U.S. aid official said on Friday.',
                'key': 'U.S. Aims to Boost Electricity in Iraq to 20 Hours',
                'key_md5': 'a249e2ce2386a60758c8030e18074f1f'
            },
            {
                'document': 'A couple of years ago Sheikh Zayed ibn Sultan Al-Nahyan, the emir of Abu Dhabi and president of the United Arab Emirates (UAE) patronized the translation and publication of an old Islamic text about the ideal prince.',
                'key': 'Editorial: The Ideal Prince',
                'key_md5': '971e682dc26433bb5a2e6fea9dd0728a'
            },
            {
                'document': 'Most Australians send text messages over mobile phones. Deaf residents find the technology provides a crucial link to the hearing world and Analysts believe messaging could soon have a similar impact in the United States. By Patrick Gray.',
                'key': 'Deaf Benefit Greatly from SMS',
                'key_md5': '86ccaf19ee0deee79f7139b6e12cacf8'
            },
            {
                'document': ' TOKYO (Reuters) - Japan and the United States agreed on  Saturday to resume imports of some American beef, halted since  December after a case of mad cow disease in Washington state,  but did not set a date for restarting trade.',
                'key': 'Japan, U.S. to Resume Some Beef Imports',
                'key_md5': '8548946f42d4e4f656f69bc22c58a65e'
            }
        ]
    }
    assert response.json() == expected
