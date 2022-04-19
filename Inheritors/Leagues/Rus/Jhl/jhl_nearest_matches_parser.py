from interface_class import Parser
from bs4 import BeautifulSoup
import requests
import json

class JhlNearestMatches(Parser):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _get_request(self) -> None:
        src = requests.get(self.args[0])
        self.response = src.text

    def _parse_data(self) -> None:
        soup = BeautifulSoup(self.response, 'lxml')
        matches_scroll = soup.find(class_='top_calendar_wrapper_load')
        print(matches_scroll)

    def call(self):
        self._get_request()
        self._parse_data()

def run():
    jhl_nearest = JhlNearestMatches('https://mhl.khl.ru/')
    jhl_nearest.call()