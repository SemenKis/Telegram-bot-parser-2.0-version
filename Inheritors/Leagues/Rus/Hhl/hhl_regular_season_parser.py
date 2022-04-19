import requests
from interface_class import Parser
from bs4 import BeautifulSoup

FILE_PATH_PREFIX = 'Rus/Hhl/hhl_reg_season.json'

class HhlRegularSeasonParser(Parser):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _get_request(self):
        src = requests.get(self.args[0])
        self.response = src.text

    def _parse_data(self):
        soup = BeautifulSoup(self.response, 'lxml')
        wrapper = soup.find(class_='sp-CenterWrapper')
        table_container = wrapper.find(class_='sp-Table-container')
        table = table_container.find(class_='sp-Table-tbody')

        teams_info = []
        team_data = {}
        team_data['records'] = []

        for team_info in table:
            team_standing = team_info.find(class_='sp-Table-cell').text
            team_name = team_info.find(class_='sp-ImageWithName__name').text
            team_logo = team_info.find(class_='sp-ImageWithName__image').find('img')
            score = team_info.find_all(class_='sp-Table-cell')

            gp = score[2].text
            w = score[3].text

            team_data['records'].append({
                "logo": f"https:{team_logo['src']}",
                "team-position": team_standing,
                "team-name": team_name,
                "И": gp,
                "В": w,
                "ВО": score[4].text,
                "П": score[5].text,
                "ПО": score[6].text,
                "Ш": score[7].text,
                "О": score[8].text,
            })
        teams_info.append(team_data)
        super()._convert_to_json(f'{Parser.path}/{FILE_PATH_PREFIX}', teams_info)

    def call(self):
        self._get_request()
        self._parse_data()

url = 'https://www.sport-express.ru/hockey/L/vhl/2021-2022/'
url2 = 'https://www.vhlru.ru/standings/regular/'

def run():
    vhl_regular_season = HhlRegularSeasonParser(url)
    vhl_regular_season.call()