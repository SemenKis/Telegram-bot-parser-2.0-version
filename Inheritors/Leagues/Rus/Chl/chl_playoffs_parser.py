from interface_class import Parser
from bs4 import BeautifulSoup
import requests

FILE_PATH_PREFIX = 'Rus/Chl/chl_playoffs.json'

class ChlPlayoffsParser(Parser):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _get_request(self):
        src = requests.get(self.args[0])
        self.response = src.text

    def _parse_data(self):
        soup = BeautifulSoup(self.response, 'lxml')
        playoffs_tables = soup.find_all(class_='b-wide_block m-not_pad b-match_tables')
        final_series = playoffs_tables[0].find('table')
        teams = final_series.find_all('tr')[1:]

        playoffs_data = []
        teams_info_dict = {}
        teams_info_dict['teams'] = []
        teams_info_dict['records'] = []

        for team in teams:
            team_data = team.find_all('td')
            team_name = team_data[1].text.strip()
            teams_info_dict['teams'].append(team_name)
            for team_data_item in team_data[2:-1]:
                if team_data_item.text.strip() == "":
                    continue
                teams_info_dict['records'].append(team_data_item.text.strip())
        playoffs_data.append(teams_info_dict)
        super()._convert_to_json(f'{Parser.path}/{FILE_PATH_PREFIX}', playoffs_data)

    def call(self):
        self._get_request()
        self._parse_data()

def run():
    chl_playoffs = ChlPlayoffsParser('https://www.khl.ru/standings/1098/playoff/')
    chl_playoffs.call()