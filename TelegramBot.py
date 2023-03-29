import telebot
from telebot import types

bot = telebot.TeleBot('6277583836:AAFxW5ZBzKEpWqoMANc19kFNHpXdiCZQMy0')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет! Я твой бот-поздравитель!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Получить поздравление с годовщиной')
        btn2 = types.KeyboardButton('Просто комплимент')
        btn3 = types.KeyboardButton('Признание в любви')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Задай интересующий тебя вопрос', reply_markup=markup) #ответ бота

    elif message.text == 'Получить поздравление с годовщиной':
        bot.send_message(message.from_user.id, 'Я поздравляю тебя с нашей шестой годовщиной свадьбы! Пусть у нас не всегда всё хорошо, но я счаслив быть с тобой!', parse_mode='Markdown')
    elif message.text == 'Просто комплимент':
        bot.send_message(message.from_user.id, 'Ты очень красивая!', parse_mode='Markdown')
    elif message.text == 'Признание в любви':
        bot.send_message(message.from_user.id, 'Я тебя люблю несмотря ни на что!', parse_mode='Markdown')

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
