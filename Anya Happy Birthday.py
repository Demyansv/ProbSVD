import telebot
from telebot import types

bot = telebot.TeleBot('5810968105:AAHnrwayh7O4VNbIBFWnLiWw1Vg9cohs8vo')

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
        btn1 = types.KeyboardButton('❓Я и мой создатель желаем тебе удачи во всём')
        btn2 = types.KeyboardButton('❓А также счастья в личной жизни')
        btn3 = types.KeyboardButton('❓И конечно же успехов в профессии')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓С чего начнёшь?)', reply_markup=markup)

    elif message.text == '❓Я и мой создатель желаем тебе удачи во всём':
        bot.send_message(message.from_user.id, '🎊Желаю тебе море позитива, отличного настроения и только лучшего на жизненном пути!', parse_mode='Markdown')
    elif message.text == '❓А также счастья в личной жизни':
        bot.send_message(message.from_user.id, '❤Пусть твой дом наполняет любовь, у тебя и твоих родных будет крепкое здоровье и в твоей семье царит гормония!', parse_mode='Markdown')
    elif message.text == '❓И конечно же успехов в профессии':
        bot.send_message(message.from_user.id, '❤Ты на правильном пути, становись только лучше, пусть в геометрической прогрессии растёт количесвто клиентов! Верь в себя! С Днём Рождения!', parse_mode='Markdown')

bot.polling(none_stop=True, interval=0)
