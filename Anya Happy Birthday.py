import telebot
from telebot import types

bot = telebot.TeleBot('5810968105:AAHnrwayh704VNbIBFWnLiW')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋Привет! Я твой бот-поздравитель! Я и мой создатель поздравляем тебя с днём рождения, и желаем:", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👋Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('❓Удачи во всём (нажми меня)')
        btn2 = types.KeyboardButton('❓Счастья в личной жизни (тоже нажми)')
        btn3 = types.KeyboardButton('❓Успехов в профессии (и на меня тоже)')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓С чего начнёшь?)', reply_markup=markup) #ответ бота

    elif message.text == '❓Удачи во всём (нажми меня)':
        bot.send_message(message.from_user.id, '🎊Желаю тебе удачи во всём, улыбок, хорошего настроения и море позитива каждый день!', parse_mode='Markdown')
    elif message.text == '❓Счастья в личной жизни (тоже нажми)':
        bot.send_message(message.from_user.id, '🫦Пусть твой дом наполняет любовь, ты и твои близвие будут здоровы, а в вашей семье всегда царит гармония и поддержка!', parse_mode='Markdown')
    elif message.text == '❓Успехов в профессии (и на меня тоже)':
        bot.send_message(message.from_user.id, '❤Пусть опыт и навыки растут в геометрической прогрессии, побольше радостных клиентов и покороения новых вершин! Ты на правильном пути!', parse_mode='Markdown')

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть