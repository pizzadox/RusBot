import telebot
from telebot import types

# Подкючаем БД

# Подключаем модуль обработки ( не факт что тут, так как будeт скорее всего отдельным файлом расписано для каждого вида профиля и типа конструкии

bot = telebot.TeleBot('5882698434:AAEQiUxsNuWmO3tesY7IU1fE-t9fPIc9xCQ')

import re
szPtrn = re.compile(r'размер \d{3,4}\s\d{3,4}$')

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

    elif szPtrn.match( message.text): # размер число1 число2 (3-4х значные
        # разбираем строку , вытаскиваем два числа price = (ширина+высота)*2* цена_профиля + ширина * высота* цена полотна.
        #но надо брать формулу от заказчика
        words = message.text.split()
        a=int(words[1])
        b=int(words[2])
        bot.send_message(message.from_user.id, 'Расчётная стоимость составит: ' +  str(a*b + 2*(a+b)+1)) # формула вообще из базы должна браться
        # Вот тут вывести
    elif message.text == 'Знаю размер':
        bot.send_message(message.from_user.id, 'Укажи размеры в поле ввода текста в Миллиметрах ( ширина/высота )', parse_mode='Markdown')


        # обрабатываем ответы с условием


bot.polling(none_stop=True, interval=0) #не отключаемся после ответа