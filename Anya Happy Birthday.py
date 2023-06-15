import telebot
from telebot import types

bot = telebot.TeleBot('5810968105:AAHnrwayh704VNbIBFWnLiWw1Vg9cohs8vo')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋Привет! Я твой бот-поздравитель!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👋Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('❓Я и мой создатель желаем тебе удачи во всём (нажми меня)')
        btn2 = types.KeyboardButton('❓А также счастья в личной жизни (тоже нажми)')
        btn3 = types.KeyboardButton('❓И конечно же успехов в профессии (и на меня тоже)')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓С чего начнёшь?)', reply_markup=markup)

    elif message.text == '❓Удачи во всём (нажми меня)':
        bot.send_message(message.from_user.id, '🎊Желаю тебе море позитива и супер настроения!', parse_mode='Markdown')
    elif message.text == '❓Счастья в личной жизни (тоже нажми)':
        bot.send_message(message.from_user.id, '🫦Пусть твой дом наполняет любовь и здоровье!', parse_mode='Markdown')
    elif message.text == '❓Успехов в профессии (и на меня тоже)':
        bot.send_message(message.from_user.id, '❤Ты на правильном пути, становись только лучше!', parse_mode='Markdown')

bot.polling(none_stop=True, interval=0)
