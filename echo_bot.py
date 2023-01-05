import telebot
from telebot import types

bot = telebot.TeleBot('5882698434:AAEQiUxsNuWmO3tesY7IU1fE-t9fPIc9xCQ')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Нужно Окно')
        btn2 = types.KeyboardButton('Нужна Дверь')
        btn3 = types.KeyboardButton('Советы')
        btn4 = types.KeyboardButton('Знаю размер')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота


    elif message.text == 'Нужно Окно':
        bot.send_message(message.from_user.id, 'Вы уверены что понимаете что вам нужно ?\n \nПолный текст можно прочитать по ' + '[ссылке](https://oknarus.com/tpost/mclj26nlh1-zaklinilo-okno-chto-delat)', parse_mode='Markdown')

    elif message.text == 'Нужна Дверь':
        bot.send_message(message.from_user.id, 'Прочитать правила сайта вы можете по ' + '[ссылке](https://oknarus.com/tpost/etcd6k6t11-okna-i-pozharnaya-bezopasnost)', parse_mode='Markdown')

    elif message.text == 'Советы':
        bot.send_message(message.from_user.id, 'Подробно про советы по ' + '[ссылке](https://oknarus.com/#services)', parse_mode='Markdown')

    elif message.text == 'Знаю размер':
        bot.send_message(message.from_user.id, 'Укажи размеры в поле ввода текста в Миллиметрах ( ширина/высота )', parse_mode='Markdown')
            @bot.message_handler(content_types=['text'])
            def after_text(message):
                if message.text == '500':
                    msg = bot.send_message(message.from_user.id, 'Введите ', reply_markup=keyboard1)
                    bot.register_next_step_handler(msg, after_text_2)

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
