from interface_class import Parser
from bs4 import BeautifulSoup
import requests

FILE_PATH_PREFIX = 'Rus/Jhl/jhl_playoffs.json'

class JhlPlayoffsParser(Parser):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _get_request(self):
        scr = requests.get(self.args[0])
        self.response = scr.text

    def _parse_data(self):
        data_list = []
        playoffs_data_dict = {}
        playoffs_data_dict['records'] = []

        soup = BeautifulSoup(self.response, 'lxml')
        playoffs_table = soup.find(class_='site_table playoff')
        pt_names = playoffs_table.find_all(class_='pt_name')

        team_name = pt_names[0].text.strip()
        team_opposite_name = pt_names[1].text.strip()

        playoffs_data_dict['teams'] = [team_name, team_opposite_name]
        for item in pt_names[2:]:
            if item.text.strip() == "":
                continue
            playoffs_data_dict['records'].append(item.text.strip())
        data_list.append(playoffs_data_dict)
        super()._convert_to_json(f'{Parser.path}/{FILE_PATH_PREFIX}', data_list)

    def call(self):
        self._get_request()
        self._parse_data()

def run():
    jhl_playoffs = JhlPlayoffsParser('https://mhl.khl.ru/standings/playoff/')
    jhl_playoffs.call()


