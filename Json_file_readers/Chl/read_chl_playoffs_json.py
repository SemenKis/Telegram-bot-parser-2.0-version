import json
from telebot import TeleBot

token = '5254316199:AAG0259Rkkzmb179uY6tGW3fSQ8jLy5iBhA'
bot = TeleBot(token)

def read_chl_playoffs_json(path ,chat):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            bot.send_message(chat, f"<b>{item['teams'][0]} vs {item['teams'][1]}</b>", parse_mode='html')
            for team_records in item['records']:
                bot.send_message(chat, team_records)