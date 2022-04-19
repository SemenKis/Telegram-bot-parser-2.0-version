from telebot import TeleBot

token = '5254316199:AAG0259Rkkzmb179uY6tGW3fSQ8jLy5iBhA'
bot = TeleBot(token)

def read_shl_playoffs_json(path, chat):
    bot.send_message(chat, 'shl playoffs not started')