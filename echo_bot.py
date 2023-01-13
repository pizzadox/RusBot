import telebot
from telebot import types

# Подкючаем БД

# Подключаем модуль обработки ( не факт что тут, так как будeт скорее всего отдельным файлом расписано для каждого вида профиля и типа конструкии

bot = telebot.TeleBot('5882698434:AAEQiUxsNuWmO3tesY7IU1fE-t9fPIc9xCQ')

import re # формат ввода размера. "размер x y" или "размер x/y"
szPtrn = re.compile(r'размер \d{3,4}(\s+|/)\d{3,4}$')
isNum  = re.compile(r'^\d{3,4}$')
oknoConst = re.compile(r'окно') # переходим на выбор конструкции окна
class BotState():
    State = "start" #состоние. пока строкой, но надо это обьявлять по другому
    width=0; height =0 # перенести в стуктура данных конкретного пользователя
    def __init__(self):
        self.State = ""
    def __repr__(self):
        ans = self.State + " width %d " % self.width + " height  %d " % self.height
        return ans
b = BotState()
bStates = {} # bStates[userid]
import okno #формулы от заказчика

@bot.message_handler(commands=['debug'])
def dbg(message):
    print (bStates)
    bot.send_message(message.from_user.id, 'DBG OK')
@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id not in bStates.keys():
        bStates[message.from_user.id] = BotState()
        print (message.from_user.id)  #dbg
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.from_user.id not in bStates.keys():
        bStates[message.from_user.id] = BotState()
        print (message.from_user.id)  #dbg
    b = bStates[message.from_user.id]  # ссылка, не копия, по идее. т.е. пункт списка изменться должен

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('окно')
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
    # выбор окна
    elif oknoConst.match(message.text):
        oknoConstr = []
        oknoConstr = okno.window
        print(oknoConstr)

        name = oknoConstr[0]
        description = okno.window(1)
        image = okno.window(2)
        print(name, description, image, oknoConstr)
        bot.send_message(message.from_user.id, 'Считаем Окно', parse_mode='Markdown')

    elif szPtrn.match( message.text): # размер число1 число2 (3-4х значные
        words = message.text.split()
        a=int(words[1])
        b=int(words[2])
        otvet = okno.answer(a,b)
        # from okno import window_filling on begin this file
        bot.send_message(message.from_user.id,  "___\n"  + otvet)
        # Вот тут вывести
    elif isNum.match( message.text):
        num = int(message.text) # здесь точно число
        if b.State == 'get_size': # Сначала ширина
            bot.send_message(message.from_user.id, "Ширина составила %d мм. Теперь введите высоту" % num)
            b.width = num; b.State = "know_width"
        elif b.State == 'know_width': # ширину знаем. теперь высоту
            b.height = num; b.State ='know_size'
            otvet = okno.answer(b.width, b.height)
            bot.send_message(message.from_user.id,otvet)
    elif message.text == 'Знаю размер':
        if b.State != 'know_size':
            bot.send_message(message.from_user.id, 'Ширина составит :', parse_mode='Markdown')
            b.State = "get_size"
        else:
            otvet = okno.answer(b.width, b.height)
            bot.send_message(message.from_user.id, otvet)
            b.State = '' # сброс на всякий случай


        # обрабатываем ответы с условием
bot.polling(none_stop=True, interval=0) #не отключаемся после ответа
