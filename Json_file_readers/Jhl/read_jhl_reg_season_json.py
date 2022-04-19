import json
from telebot import TeleBot

token = '5254316199:AAG0259Rkkzmb179uY6tGW3fSQ8jLy5iBhA'
bot = TeleBot(token)

def read_jhl_reg_season_json(path, chat):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            bot.send_message(chat, f"<b>{item['conference']}</b>", parse_mode='html')
            for team_info in item['records']:
                bot.send_photo(chat, f"{team_info['logo']}")
                bot.send_message(chat, f"{team_info['team-position']},  {team_info['team-name']} \n"
                                       f"И: {team_info['И']}\n"
                                       f"В: {team_info['В']}\n"
                                       f"ВО: {team_info['ВО']}\n"
                                       f"П: {team_info['П']}\n"
                                       f"ПО: {team_info['ПО']}\n"
                                       f"Ш: {team_info['Ш']}\n"
                                       f"О: {team_info['О']}\n")