import json

import telebot
from telebot import types

# Подкючаем БД

# Подключаем модуль обработки ( не факт что тут, так как будeт скорее всего отдельным файлом расписано для каждого вида профиля и типа конструкии

bot = telebot.TeleBot('5882698434:AAEQiUxsNuWmO3tesY7IU1fE-t9fPIc9xCQ')

import re # формат ввода размера. "размер x y" или "размер x/y"
szPtrn = re.compile(r'(^размер\s+|^\s*)(\d{3,4})(\s+|/)(\d{3,4})\s*$')
isNum  = re.compile(r'^\d{3,4}$')
oknoConst = re.compile(r'окно') # переходим на выбор конструкции окна
class BotState():
    State = "start" #состоние. пока строкой, но надо это обьявлять по другому
    width=0; height =0 # перенести в стуктура данных конкретного пользователя
    construction_id = 0 #orders.db construction id
    def __init__(self):
        self.State = ""
    def __repr__(self):
        ans = self.State + " width %d " % self.width + " height  %d " % self.height
        return ans
def mrkpMenu(*btns): # Меню с кнопкапи. Заголовки кнопок через запятую
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
    for label in btns:
       markup.add(label)
    return markup
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
        markup = mrkpMenu('окно','Нужна Дверь','Советы','Знаю размер')
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота

    elif message.text == 'Нужно Окно':
        bot.send_message(message.from_user.id, 'Вы уверены что понимаете что вам нужно ?\n \nПолный текст можно прочитать по ' + '[ссылке](https://oknarus.com/tpost/mclj26nlh1-zaklinilo-okno-chto-delat)', parse_mode='Markdown')

    elif message.text == 'Нужна Дверь':
        bot.send_message(message.from_user.id, 'Прочитать правила сайта вы можете по ' + '[ссылке](https://oknarus.com/tpost/etcd6k6t11-okna-i-pozharnaya-bezopasnost)', parse_mode='Markdown')

    elif message.text == 'Советы':
        bot.send_message(message.from_user.id, 'Подробно про советы по ' + '[ссылке](https://oknarus.com/#services)', parse_mode='Markdown')
    # выбор окна
    elif oknoConst.match(message.text): #окно
        oknoConstr = []
        oknoConstr = okno.window()
        #print(oknoConstr)
        markup = types.InlineKeyboardMarkup()
        for r in oknoConstr:
            name = r[0]
            description = r[1]
            image = r[2]
            markup.add( types.InlineKeyboardButton(text=r[0] , callback_data = '{"user_id": %d,' % message.from_user.id + '"okno": %d}' % r[3]))
        bot.send_message(message.from_user.id, "Выиурите тип",reply_markup=markup)
        #bot.send_message(message.from_user.id, 'Считаем Окно %s' % name, parse_mode='Markdown')

    elif mt := szPtrn.match( message.text): # (размер )(число1) () (число2) (3-4х значные
        a = int( mt.group(2) );b=int(mt.group(4))
        otvet = okno.answer(a,b)
        bot.send_message(message.from_user.id,   otvet)
    elif isNum.match( message.text):
        num = int(message.text) # здесь точно число
        if b.State == 'get_size': # Сначала ширина
            bot.send_message(message.from_user.id, "Ширина составила %d мм. Теперь введите высоту" % num)
            b.width = num; b.State = "know_width"
        elif b.State == 'know_width': # ширину знаем. теперь высоту
            b.height = num; b.State ='know_size'
            otvet = okno.answer(b.width, b.height)
            bot.send_message(message.from_user.id,otvet,reply_markup=mrkpMenu('Расчёт','окно')) # не всегда обе
    elif message.text == 'Знаю размер':
        if b.State != 'know_size':
            bot.send_message(message.from_user.id, 'Ширина составит :', parse_mode='Markdown')
            b.State = "get_size"
        else:
            otvet = okno.answer(b.width, b.height)
            bot.send_message(message.from_user.id, otvet)
            b.State = '' # сброс на всякий случай


        # обрабатываем ответы с условием
    elif message.text == 'Расчёт':
        ans1 = "Окно шириной %d мм" % b.width + " высотой %d мм " %b.height  +  "типа № %d \n" % b.construction_id
        if (b.height and b.width and b.construction_id):
            ans2 = okno.answer(b.width, b.height)
            markup = mrkpMenu('Поздравляю')
        else:
            ans2 = 'Недостаточно данных'
            markup = mrkpMenu('Знаю размер','окно')
        bot.send_message(message.from_user.id,ans1 + ans2,reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True) #вешаем обработчик событий на нажатие всех inline-кнопок
def callback_inline(call):
    if call.data: #//проверяем есть ли данные если да, далаем с ними что-то.
        print(call.data, call.id )
        cb=json.loads(call.data)
        ans = "Callback is working!"
        if cb['user_id'] in bStates.keys():
            print("callback for %d" % cb['user_id'])
            constr_id= int( cb['okno'] )
            print (constr_id);ans = "Вы выбрали конструкцию ID %d" % constr_id
            b = bStates[cb['user_id']]
            b.construction_id = constr_id
            b.State = "get_tip"
            bot.send_message(cb['user_id'],"Тратата!",reply_markup=mrkpMenu('Расчёт',"Знаю размер")) #не всегда обе
    bot.answer_callback_query(call.id, ans)

bot.polling(none_stop=True, interval=0) #не отключаемся после ответа
