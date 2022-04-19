from interface_class import Parser
import requests
import json

FILE_JSON_PATH_PREFIX = 'Swe/Shl/shl_reg_season_data_for_parsing.json'
FILE_PATH_PREFIX = 'Swe/Shl/shl_reg_season.json'

class ShlRegularSeasonParser(Parser):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _get_request(self):
        src = requests.get(self.args[0])
        response = src.json()
        with open(f'{Parser.path}/{FILE_JSON_PATH_PREFIX}', 'w', encoding='utf-8') as file:
            json.dump(response, file, indent=4, ensure_ascii=False)

    def _parse_data(self):
        with open(f'{Parser.path}/{FILE_JSON_PATH_PREFIX}', 'r', encoding='utf-8') as file:
            data = json.load(file)
            teams_info = []
            team_data = {}
            for item in data:
                team_data['records'] = []
                for team_info in item['stats']:
                    team_name = team_info['TeamCode']
                    team_standing = team_info['Rank']
                    gp = team_info['GP']
                    g = team_info['G']
                    ga = team_info['GA']
                    nonregw = team_info['NonRegW']
                    regw = team_info['RegW']
                    regl = team_info['RegL']
                    diff = team_info['Diff']
                    pts = team_info['Points']

                    team_data['records'].append({
                        "team-position": team_standing,
                        "team-name": team_name,
                        "GP": gp,
                        "REGW": regw,
                        "NONREGW": nonregw,
                        "REGL": regl,
                        "G": g,
                        "GA": ga,
                        "DIFF": diff,
                        "PTS": pts
                    })
                teams_info.append(team_data)
            with open(f'{Parser.path}/{FILE_PATH_PREFIX}', 'w', encoding='utf-8') as file:
                json.dump(teams_info, file, ensure_ascii=False, indent=4)

    def call(self):
        self._get_request()
        self._parse_data()

def run():
    url = 'https://www.shl.se/p/api/statistics/' \
          'standings_standings?ssgtUuid=qZl-8qb98ZuHk&count=25'

    shl_regular_season = ShlRegularSeasonParser(url)
    shl_regular_season.call()