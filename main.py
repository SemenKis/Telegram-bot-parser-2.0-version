from telebot import TeleBot
from telebot import types
from caller import call_parser

token = '5254316199:AAG0259Rkkzmb179uY6tGW3fSQ8jLy5iBhA'

bot = TeleBot(token)

def return_inline_keybroad():
    markup = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(callback_data='hhl', text='HHL (Russian high hockey league)')
    button_2 = types.InlineKeyboardButton(callback_data='jhl', text='JHL (Russian junior hockey league)')
    button_3 = types.InlineKeyboardButton(callback_data='chl', text='CHL (Russian continental hockey league)')
    button_4 = types.InlineKeyboardButton(callback_data='nhl', text='NHL (National hockey league)')
    button_5 = types.InlineKeyboardButton(callback_data='shl', text='SHL (Swedish hockey league)')
    markup.add(button_1, button_2, button_3, button_4, button_5)
    return markup

def return_reply_keybroad(text):
    markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    button_1 = types.KeyboardButton(f'{text} playoffs')
    button_2 = types.KeyboardButton(f'{text} regular season')
    menu_button = types.KeyboardButton('menu')
    markup.add(button_1, button_2, menu_button)
    return markup

@bot.message_handler(commands='start')
def start(message):
    bot.send_message(message.chat.id, "Hi")

@bot.message_handler(commands='show')
def show(message):
    bot.send_message(message.chat.id, "choose", reply_markup=return_inline_keybroad())

@bot.callback_query_handler(func=lambda c: True)
def callback(call):
    if call.data == 'hhl':
        bot.send_message(call.message.chat.id, "Hi", reply_markup=return_reply_keybroad('HHL'))

    if call.data == 'jhl':
        bot.send_message(call.message.chat.id, "Hi", reply_markup=return_reply_keybroad('JHL'))

    if call.data == 'chl':
        bot.send_message(call.message.chat.id, "Hi", reply_markup=return_reply_keybroad('CHL'))

    if call.data == 'nhl':
        bot.send_message(call.message.chat.id, "Hi", reply_markup=return_reply_keybroad('NHL'))

    if call.data == 'shl':
        bot.send_message(call.message.chat.id, "Hi", reply_markup=return_reply_keybroad('SHL'))

@bot.message_handler(content_types='text')
def answer(message):
    call_parser(message.text, message.chat.id)
    if message.text == 'menu':
        bot.send_message(message.chat.id, '<b>you can choose again 👇🏻</b>', parse_mode='html',
                         reply_markup=return_inline_keybroad())


bot.polling(non_stop=True)