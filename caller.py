from Inheritors.Leagues.Rus.Jhl import jhl_regular_season_parser, jhl_playoffs_parser
from Inheritors.Leagues.Rus.Chl import nearest_matches_parser, chl_regular_season_parser, chl_playoffs_parser
from Inheritors.Leagues.Rus.Hhl import hhl_playoffs_parser, hhl_regular_season_parser
from Inheritors.Leagues.Usa.Nhl import nhl_regular_season_parser
from Inheritors.Leagues.Swe.Shl import shl_regular_season_parser

from Json_file_readers.Hhl.read_hhl_playoffs_json import read_hhl_playoffs_json
from Json_file_readers.Hhl.read_hhl_reg_season_json import read_hhl_reg_season_json
from Json_file_readers.Jhl.read_jhl_playoffs_json import read_jhl_playoffs_json
from Json_file_readers.Jhl.read_jhl_reg_season_json import read_jhl_reg_season_json
from Json_file_readers.Chl.read_chl_playoffs_json import read_chl_playoffs_json
from Json_file_readers.Chl.read_chl_reg_season_json import read_chl_reg_season_json
from Json_file_readers.Nhl.read_nhl_reg_season_json import read_nhl_reg_season_json
from Json_file_readers.Nhl.read_nhl_playoffs_json import read_nhl_playoffs_json
from Json_file_readers.Shl.read_shl_reg_season import read_shl_reg_season_json
from Json_file_readers.Shl.read_shl_playoffs_json import read_shl_playoffs_json

PATH_TO_JSON_FILES = 'Data/json_files/json_leagues'

def call_parser(parser_name, chat):
    if parser_name == 'HHL playoffs':
        call_hhl_parser('playoffs', chat)
    if parser_name == 'HHL regular season':
        call_hhl_parser('regular season', chat)
    if parser_name == 'JHL playoffs':
        call_jhl_parser('playoffs', chat)
    if parser_name == 'JHL regular season':
        call_jhl_parser('regular season', chat)
    if parser_name == 'CHL playoffs':
        call_chl_parser('playoffs', chat)
    if parser_name == 'CHL regular season':
        call_chl_parser('regular season', chat)
    if parser_name == 'NHL playoffs':
        call_nhl_parser('playoffs', chat)
    if parser_name == 'NHL regular season':
        call_nhl_parser('regular season', chat)
    if parser_name == 'SHL playoffs':
        call_shl_parser('playoffs', chat)
    if parser_name == 'SHL regular season':
        call_shl_parser('regular season', chat)

def call_hhl_parser(parser_type, chat):
    if parser_type == 'playoffs':
        hhl_playoffs_parser.run()
        read_hhl_playoffs_json(f'{PATH_TO_JSON_FILES}/Rus/Hhl/hhl_playoffs.json', chat)
    elif parser_type == 'regular season':
        hhl_regular_season_parser.run()
        read_hhl_reg_season_json(f'{PATH_TO_JSON_FILES}/Rus/Hhl/hhl_reg_season.json', chat)

def call_jhl_parser(parser_type, chat):
    if parser_type == 'playoffs':
        jhl_playoffs_parser.run()
        read_jhl_playoffs_json(f'{PATH_TO_JSON_FILES}/Rus/Jhl/Jhl_playoffs.json', chat)
    elif parser_type == 'regular season':
        jhl_regular_season_parser.run()
        read_jhl_reg_season_json(f'{PATH_TO_JSON_FILES}/Rus/Jhl/Jhl_reg_season.json', chat)

def call_chl_parser(parser_type, chat):
    if parser_type == 'playoffs':
        chl_playoffs_parser.run()
        read_chl_playoffs_json(f'{PATH_TO_JSON_FILES}/Rus/Chl/Chl_playoffs.json', chat)
    elif parser_type == 'regular season':
        chl_regular_season_parser.run()
        read_chl_reg_season_json(f'{PATH_TO_JSON_FILES}/Rus/Chl/Chl_reg_season.json', chat)

def call_nhl_parser(parser_type, chat):
    if parser_type == 'playoffs':
        read_nhl_playoffs_json('', chat)
    elif parser_type == 'regular season':
        nhl_regular_season_parser.run()
        read_nhl_reg_season_json(f'{PATH_TO_JSON_FILES}/Usa/Nhl/nhl_reg_season.json', chat)

def call_shl_parser(parser_type, chat):
    if parser_type == 'playoffs':
        read_shl_playoffs_json('', chat)
    elif parser_type == 'regular season':
        shl_regular_season_parser.run()
        read_shl_reg_season_json(f'{PATH_TO_JSON_FILES}/Swe/Shl/shl_reg_season.json', chat)