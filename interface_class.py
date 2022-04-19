from abc import ABC
from abc import abstractmethod
import json

# path = 'Data/json_files/json_leagues/Rus/hhl_reg_season.json'

class Parser(ABC):
    count_subclasses = 0
    path = 'Data/json_files/json_leagues/'

    def __init__(self):
        Parser.count_subclasses += 1

    @abstractmethod
    def _get_request(self) -> None:
        pass

    @abstractmethod
    def _parse_data(self) -> None:
        pass

    def _convert_to_json(self, path, obj):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(obj, file, indent=4, ensure_ascii=False)

    @classmethod
    def count(cls):
        print(f"Inheritors count: {cls.count_subclasses}")