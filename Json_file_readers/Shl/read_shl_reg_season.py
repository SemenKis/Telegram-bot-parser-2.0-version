import json

from telebot import TeleBot

token = '5254316199:AAG0259Rkkzmb179uY6tGW3fSQ8jLy5iBhA'
bot = TeleBot(token)

def read_shl_reg_season_json(path, chat):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            for team_info in item['records']:
                bot.send_message(chat, f"<b>{team_info['team-position']} | {team_info['team-name']}</b>\n"
                                       f"GP: {team_info['GP']}\n"
                                       f"REGW: {team_info['REGW']}\n"
                                       f"NONREGW: {team_info['NONREGW']}\n"
                                       f"REGL: {team_info['REGL']}\n"
                                       f"G: {team_info['G']}\n"
                                       f"GA: {team_info['GA']}\n"
                                       f"DIFF: {team_info['DIFF']}\n"
                                       f"PTS: {team_info['PTS']}\n",
                                       parse_mode='html')