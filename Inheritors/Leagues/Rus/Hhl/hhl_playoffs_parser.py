from interface_class import Parser
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

FILE_PATH_PREFIX = 'Rus/Hhl/hhl_playoffs.json'

class HhlPlayoffsParser(Parser):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _get_request(self):
        request = Request(self.args[0], headers=self.kwargs['headers'])
        self.response = urlopen(request).read()

    def _parse_data(self):
        soup = BeautifulSoup(self.response, 'lxml')
        playoffs_table_container = soup.find(class_='inner-tabs')
        playoffs_inner_table = playoffs_table_container.find(class_='inner-tabs__content show')
        playoffs_teams = playoffs_inner_table.find('tbody')
        playoffs_teams_info = playoffs_teams.find_all('tr')

        playoffs_data = []
        teams_info_dict = {}
        teams_info_dict['teams'] = []
        teams_info_dict['records'] = []

        for team in playoffs_teams_info:
            team_info = team.find_all('td')
            team_name = team_info[0].text.strip()
            teams_info_dict['teams'].append(team_name)
            for date_item in team_info[1:]:
                if date_item.text.strip() == "":
                    continue
                teams_info_dict['records'].append(date_item.text.strip())
        playoffs_data.append(teams_info_dict)
        super()._convert_to_json(f'{Parser.path}/{FILE_PATH_PREFIX}', playoffs_data)

    def call(self):
        self._get_request()
        self._parse_data()

header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
      'AppleWebKit/537.11 (KHTML, like Gecko) '
      'Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}

def run():
    hhl_playoffs = HhlPlayoffsParser('https://www.vhlru.ru/standings/playoff/', headers=header)
    hhl_playoffs.call()
