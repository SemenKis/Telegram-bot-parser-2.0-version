import json
from telebot import TeleBot

token = '5254316199:AAG0259Rkkzmb179uY6tGW3fSQ8jLy5iBhA'
bot = TeleBot(token)

def read_nhl_reg_season_json(path, chat):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            bot.send_message(chat, f"<b>{item['conference']} {item['division']}</b>", parse_mode='html')
            for team in item['records']:
                bot.send_message(chat, f"{team['team-position']} | <b>{team['team-name']}</b> \n"
                                       f"GP: {team['GP']} \n"
                                       f"W: {team['W']} \n"
                                       f"L: {team['L']} \n"
                                       f"OT: {team['OT']} \n"
                                       f"PTS: {team['PTS']} \n"
                                       f"RW: {team['RW']} \n"
                                       f"ROW: {team['ROW']} \n"
                                       f"GF: {team['GF']} \n"
                                       f"GA: {team['GA']}", parse_mode='html')