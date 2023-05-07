import telebot, random, datetime, time
from datetime import datetime, timedelta
from random import randint
from telebot import types

tb = telebot.TeleBot('5648742212:AAEs2f_OCHgw0oq6aPpwoKzU1pcQYjlPze8')


@tb.message_handler(commands=['start'])
def start(message):
    global admlist
    admlist = [1409320209]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    hello = types.KeyboardButton('Приветствие')
    groups = types.KeyboardButton('Выбрать группу')
    games = types.KeyboardButton('Мини-игры')
    teach = types.KeyboardButton('Для преподавателей')
    info = types.KeyboardButton('Обо мне')
    admin = types.KeyboardButton('.AMpanel')
    if message.chat.id not in admlist:
        markup.add(hello, groups, games, teach, info)
    elif message.chat.id in admlist:
        markup.add(hello, groups, games, teach, info, admin)
    say = tb.send_message(message.chat.id, f"<i>Привет!</i>  Это КАИТ, мои возможности:", parse_mode="html", reply_markup=markup)
    tb.register_next_step_handler(say, move)


def move(message):
    mov = message.text
    if message.chat.id in admlist and mov == ".AMpanel":
        admpanel(message)
    elif mov == 'Приветствие':
        say = tb.send_message(message.chat.id, "Привет. Я Каитий, создан для быстрого доступа к информации :) Продолжим? Меню снизу...", parse_mode="html")
        tb.register_next_step_handler(say, move)
    elif mov == ':55-':
        message.text = "ИСП-151/д"
        isp(message)
    elif mov == 'Выбрать группу':
        groups(message)
    elif mov == 'Для преподавателей':
        teachlist(message)
    elif mov == 'Обо мне':
        say = tb.send_message(message.chat.id, f"""Биография:
  <b>Имя:</b> Каитий
  <b>Цель:</b> Помочь студентам
  ориентироваться
  в ГБПОУ КАИТ №20.
  <b>Задача:</b> Предоставлять всю
  информацию о звонках и парах
  колледжа и некоторые
  другие возможности :)

  <b>Дата начала
  разработки:</b> 30.10.2022

  <b>Версия:</b> Prod. 2.9.4
  <b>Последнее обновление:</b> 10.02.2023

  <i>Cтолкнулись с
  тех. неполадками, или же
  у вас есть классные идеи
  для обновлений? - просьба писать:</i>
  <b>Cюды:</b> @kpectox (ТГ)
  <b>Либо сюды:</b> LaFFerty#6395 (ДС)""", parse_mode="html")
        tb.register_next_step_handler(say, move)
    elif mov == 'Мини-игры':
        listgames(message)
    else:
        say = tb.send_message(message.chat.id, f"Неизвестная команда, попробуй еще раз.", parse_mode="html")
        tb.register_next_step_handler(say, move)
    loggy(message.chat.id, message.from_user.first_name, message.from_user.username, message.text)
    file_user_id(message.from_user.username, message.chat.id, timed)


def loggy(ide, name, tag, mess):
    global timed
    timed = (datetime.now() + timedelta(hours=3)).strftime('%H:%M:%S || %d.%m.%Y')
    print(f"""- - - - - - - - - - - - - - -
id: {ide}
Ник: {name}  тэг: ({tag})
mess: {mess}
Посещение: {timed}
- - - - - - - - - - - - - - -""")

def file_user_id(user, uid, timed):
    flag = 0
    with open('users.txt') as f:
        for line in f:
            if str(uid) in line:
                flag = 1
                f.close()
                with open ('users.txt', 'r') as file:
                    old = file.read()
                new = old.replace(line, "User: {}, id: {}, Last on: {}\n".format(user, uid, timed))
                with open('users.txt', 'w') as f:
                    f.write(new)
                break
    if flag == 0:
        file = open("users.txt", "a")
        file.write("User: {}, id: {}, Last on: {}\n".format(user, uid, timed))
        file.close()
        f = open('ides.txt', 'a')
        f.write(str(uid) + '\n')
        f.close()


def admpanel(message):
    markup10 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    spam = types.KeyboardButton('Рассылка')
    speed = types.KeyboardButton('Quick')
    rannum = types.KeyboardButton('RandNum')
    back = types.KeyboardButton('BACK')
    markup10.add(spam, speed, rannum, back)
    say = tb.send_message(message.chat.id, f"God Mode menu:", parse_mode="html", reply_markup=markup10)
    tb.register_next_step_handler(say, admove)


def admove(message):
    mov = message.text
    if mov == 'Рассылка':
        say = tb.send_message(message.chat.id, f"Подтвердить?", parse_mode="html")
        tb.register_next_step_handler(say, prespam)
    elif mov == 'Quick':
        message.text = "ИСП-151/д"
        isp(message)
    elif mov == 'Весна':
        say = tb.send_message(message.chat.id, f"Время (с)?", parse_mode="html")
        tb.register_next_step_handler(say, event)
    elif mov == 'BACK':
        start(message)


def event(message):
    time.sleep(int(message.text))
    f = open('ides.txt', 'r')
    data = f.readlines()
    for i in data:
        tb.send_message(i, f"""Пришла и оторвала голову нам чумачечая весна
И нам не до сна
И от любви схожу я с ума
Чумачечая весна, ЧуМАчеЧая

С первым днем весны!""", parse_mode="html")
    f.close()
    admove(message)


def prespam(message):
    if message.text == "Да":
        say = tb.send_message(message.chat.id, f"Текст сообщения:", parse_mode="html")
        tb.register_next_step_handler(say, spam)
    else:
        say = tb.send_message(message.chat.id, f"Команда отменена", parse_mode="html")
        tb.register_next_step_handler(say, admove)

def spam(message):
    f = open('ides.txt', 'r')
    data = f.readlines()
    for i in data:
        tb.send_message(i, message.text)
    f.close()
    admove(message)


def listgames(message):
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bonegame = types.KeyboardButton('Кости')
    twentyone = types.KeyboardButton('21-а точка')
    doors = types.KeyboardButton('Двери')
    randomer = types.KeyboardButton('Рандом')
    back = types.KeyboardButton('На главную')
    markup3.add(bonegame, twentyone, doors, randomer, back)
    say = tb.send_message(message.chat.id, f"""Список доступных развлечений:""", reply_markup=markup3)
    tb.register_next_step_handler(say, games)


def games(message):
    mov = message.text
    if mov in ['Кости', '21-а точка', 'Двери','Рандом']:
        loggy(message.chat.id, message.from_user.first_name, message.from_user.username, message.text)
    if mov == 'Кости':
        bonemenu(message)
    elif mov == ":55-":
        message.text = ".ИСП-151/д"
        isp(message)
    elif mov == '21-а точка':
        twentyonemenu(message)
    elif mov == 'Двери':
        menudoors(message)
    elif mov == 'Рандом':
        say = tb.send_message(message.chat.id, f"""Диапазон:
        пример (4-11)""")
        tb.register_next_step_handler(say, randomer)
    elif mov == 'На главную':
        start(message)
    else:
        say = tb.send_message(message.chat.id, f"Неизвестная команда, попробуй еще раз.", parse_mode="html")
        tb.register_next_step_handler(say, games)


def menudoors(message):
    markup12 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton('Начать')
    rules = types.KeyboardButton('Правила')
    back = types.KeyboardButton('На главную')
    markup12.add(start, rules, back)
    say = tb.send_message(message.chat.id, f"""Игра в двери:""", reply_markup=markup12)
    tb.register_next_step_handler(say, doorsguide)


def doorsguide(message):
    txt = message.text
    if txt == 'Начать':
        lvl = 1
        doors(message, lvl)
    elif txt == ":55-":
        message.text = "ИСП-151/д"
        isp(message)
    elif txt == 'Правила':
        say = tb.send_message(message.chat.id, f"""Каждый раунд игрок выбирает одну из дверей.
Цель - выжить.""")
        tb.register_next_step_handler(say, doorsguide)
    elif txt == 'На главную':
        listgames(message)
    else:
        say = tb.send_message(message.chat.id, f"Неизвестная команда, попробуй еще раз.", parse_mode="html")
        tb.register_next_step_handler(say, menudoors)


def doors(message, lvl):
    markup13 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    door1 = types.KeyboardButton('1-я Дверь')
    door2 = types.KeyboardButton('2-я Дверь')
    door3 = types.KeyboardButton('3-я Дверь')
    back = types.KeyboardButton('На главную')
    markup13.add(door1, door2, door3, back)
    say = tb.send_message(message.chat.id, f"""<b>Раунд {lvl}</b>
  Выбери дверь:""", reply_markup=markup13, parse_mode="html")
    tb.register_next_step_handler(say, ansdoors, lvl)


def ansdoors(message, lvl):
    lvl += 1
    erdoor = randint(1, 3)
    txt = message.text
    if lvl <= 10:
        if txt == '1-я Дверь':
            if erdoor == 1:
                tb.send_message(message.chat.id, f"За дверью оказалась смЭрть", parse_mode="html")
                tb.send_message(message.chat.id, f"Вы дошли до {lvl - 1} уровня", parse_mode="html")
                menudoors(message)
            else:
                tb.send_message(message.chat.id, f"За дверью никого не оказалось\n Вы молча прошли дальше..", parse_mode="html")
                doors(message, lvl)
        elif txt == "2-я Дверь":
            if erdoor == 2:
                tb.send_message(message.chat.id, f"За дверью оказалась смЭрть", parse_mode="html")
                tb.send_message(message.chat.id, f"Вы дошли до {lvl - 1} уровня", parse_mode="html")
                menudoors(message)
            else:
                tb.send_message(message.chat.id, f"За дверью никого не оказалось\n Вы молча прошли дальше..", parse_mode="html")
                doors(message, lvl)
        elif txt == '3-я Дверь':
            if erdoor == 3:
                tb.send_message(message.chat.id, f"За дверью оказалась смЭрть", parse_mode="html")
                tb.send_message(message.chat.id, f"Вы дошли до {lvl - 1} уровня", parse_mode="html")
                menudoors(message)
            else:
                tb.send_message(message.chat.id, f"За дверью никого не оказалось\n Вы молча прошли дальше..", parse_mode="html")
                doors(message, lvl)
        elif txt == '4-я Дверь' and lvl > 10:
            if erdoor == 4:
                tb.send_message(message.chat.id, f"За дверью оказалась смЭрть", parse_mode="html")
                tb.send_message(message.chat.id, f"Вы дошли до {lvl - 1} уровня", parse_mode="html")
                menudoors(message)
            else:
                tb.send_message(message.chat.id, f"За дверью никого не оказалось\n Вы молча прошли дальше..", parse_mode="html")
                doors(message, lvl)
        elif txt == '5-я Дверь' and lvl > 10:
            if erdoor == 5 :
                tb.send_message(message.chat.id, f"За дверью оказалась смЭрть", parse_mode="html")
                tb.send_message(message.chat.id, f"Вы дошли до {lvl - 1} уровня", parse_mode="html")
                menudoors(message)
            else:
                tb.send_message(message.chat.id, f"За дверью никого не оказалось\n Вы молча прошли дальше..", parse_mode="html")
                doors(message, lvl)
        elif txt == 'На главную':
            menudoors(message)
        else:
            say = tb.send_message(message.chat.id, f"Неизвестная команда, попробуй еще раз.", parse_mode="html")
            lvl -= 1
            tb.register_next_step_handler(say, ansdoors, lvl)
    elif lvl > 10:
        tb.send_message(message.chat.id, f"Вы прошли игру\n Поздравляю!", parse_mode="html")
        menudoors(message)



def bonemenu(message):
    markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton('Бросить кубики')
    rules = types.KeyboardButton('Правила')
    back = types.KeyboardButton('На главную')
    markup4.add(start, rules, back)
    say = tb.send_message(message.chat.id, f"""Игра в кости:""", reply_markup=markup4)
    tb.register_next_step_handler(say, bonegame)


def bonegame(message):
    mov = message.text
    if mov == 'Бросить кубики':
        a, b, c, d = randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)
        tb.send_message(message.chat.id, f"Вы выбросили {a} и {b} ({a + b}) ", parse_mode="html")
        tb.send_message(message.chat.id, f"Бот выкинул {c} и {d} ({c + d}) ", parse_mode="html")
        if a + b > c + d:
            say = tb.send_message(message.chat.id, f"Вы выиграли!!", parse_mode="html")
        elif a + b == c + d:
            say = tb.send_message(message.chat.id, f"Ничья, увы", parse_mode="html")
        else:
            say = tb.send_message(message.chat.id, f"Увы, вы проиграли...", parse_mode="html")
        tb.register_next_step_handler(say, bonegame)
    elif mov == ":55-":
        message.text = "ИСП-151/д"
        isp(message)
    elif mov == 'Правила':
        say = tb.send_message(message.chat.id, f"""Игроки кидают кубики, у кого больше сумма чисел - тот и выиграл""")
        tb.register_next_step_handler(say, bonegame)
    elif mov == 'На главную':
        listgames(message)
    else:
        say = tb.send_message(message.chat.id, f"Неизвестная команда, попробуй еще раз.", parse_mode="html")
        tb.register_next_step_handler(say, bonegame)


def twentyonemenu(message):
    markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton('Начать')
    rules = types.KeyboardButton('Правила')
    back = types.KeyboardButton('На главную')
    markup5.add(start, rules, back)
    say = tb.send_message(message.chat.id, f"""Игра в 21-у точку:""", reply_markup=markup5)
    tb.register_next_step_handler(say, twentyoneguide)


def twentyoneguide(message):
    mov = message.text
    if mov == 'Начать':
        twentyonegame(message)
    elif mov == 'Правила':
        say = tb.send_message(message.chat.id, f"""В начале игроку выдается две \nкарты с числами, игрок может взять
еще карту, но сумма их чисел \nне должна превышать 21. Бот берет \nстолько же карт. Побеждает тот, \nкто ближе всего к числу 21""")
        tb.register_next_step_handler(say, twentyoneguide)
    elif mov == 'На главную':
        listgames(message)
    elif mov == ":55-":
        message.text = "ИСП-151/д"
        isp(message)
    else:
        say = tb.send_message(message.chat.id, f"Неизвестная команда, попробуй еще раз.", parse_mode="html")
        tb.register_next_step_handler(say, twentyoneguide)


def twentyonegame(message):
    a1, b1 = randint(5, 10), randint(5, 10)
    tb.send_message(message.chat.id, f"У вас {a1} и {b1}\n   Сумма: {a1+b1}", parse_mode="html")
    markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    more = types.KeyboardButton('Ещё')
    pas = types.KeyboardButton('Пас')
    back = types.KeyboardButton('На главную')
    markup6.add(more, pas, back)
    say = tb.send_message(message.chat.id, "Ещё карту?", reply_markup=markup6)
    tb.register_next_step_handler(say, bonuscard, a1, b1)


def bonuscard(message, a1, b1):
    b2, c, d, e = randint(5, 10), randint(5, 10), randint(5, 10), randint(5, 10)
    txt = message.text
    if txt == "Ещё":
        if (a1+b1+b2) <= 21 and (c+d+e) > 21:
            c, d, e = randint(5, 9), randint(4, 8), randint(4, 10)
        elif (a1+b1+b2) > 21 and (c+d+e) > 21:
            c, d, e = randint(4, 8), randint(4, 8), randint(4, 9)
        tb.send_message(message.chat.id, f"Вам добавилась карта {b2}", parse_mode="html")
        tb.send_message(message.chat.id, f"""У вас {a1}, {b1}, {b2}\n   Сумма: {a1+b1+b2}
У бота {c}, {d}, {e}\n   Сумма: {c+d+e}""", parse_mode="html")
        if [a1, b1, b2, c, d, e].count(7) > 4:
            tb.send_message(message.chat.id, f"Вам очень повезло, шанс на такие\nчисла очень мал!", parse_mode="html")
            tb.send_message(message.chat.id, f"""Я думаю, если вы сделали что-то, \nи оно вышло довольно неплохо — вы
должны пойти и сделать что-то еще,\nне останавливаясь на месте слишком надолго. <b>Просто творите дальше.</b>""", parse_mode="html")
        elif (a1+b1+b2) == (c+d+e):
            tb.send_message(message.chat.id, f"Видимо это... Ничья", parse_mode="html")
        elif ((a1+b1+b2) > 21) and ((c+d+e) > 21):
            tb.send_message(message.chat.id, f"Вы оба перебрали, ничья", parse_mode="html")
        elif (a1+b1+b2) > 21:
            tb.send_message(message.chat.id, f"У вас перебор ({a1+b1+b2})\nВы проиграли", parse_mode="html")
        elif (c+d+e) > 21:
            tb.send_message(message.chat.id, f"У бота перебор ({c+d+e})\nПоздравляю с победой :)", parse_mode="html")
        else:
            if (a1+b1+b2) > (c+d+e):
                tb.send_message(message.chat.id, f"Поздравляю с победой!!", parse_mode="html")
            elif (a1+b1+b2) < (c+d+e):
                tb.send_message(message.chat.id, f"Вы проиграли...",parse_mode="html")
        twentyonemenu(message)
    elif txt == "Пас":
        if a1+b1 < 19 and c < 8:
            c, d = randint(8, 10), randint(7, 10)
        tb.send_message(message.chat.id, f"У вас {a1} и {b1}\n   Сумма: {a1+b1}\n\nУ бота {c} и {d}\n   Сумма: {c+d}", parse_mode="html")
        if a1 + b1 > c + d:
            tb.send_message(message.chat.id, f"Поздравляю с победой :)", parse_mode="html")
        elif a1 + b1 < c + d:
            tb.send_message(message.chat.id, f"Проигрыш, сочувствую...", parse_mode="html")
        else:
            tb.send_message(message.chat.id, f"Видимо это... Ничья", parse_mode="html")
        twentyonemenu(message)
    elif txt == "На главную":
        twentyonemenu(message)
    elif txt == ":55-":
        message.text = "ИСП-151/д"
        isp(message)
    else:
        tb.send_message(message.chat.id, f"Я не хочу так играть..", parse_mode="html")
        twentyonemenu(message)


def randomer(message):
    num = message.text
    x = num.count("-")
    n, c = num.split("-"), 0
    for i in n:
        if i.isnumeric():
            c += 1
    if num == "Кости":
        bonemenu(message)
    elif num == "Типо 21-но":
        twentyonemenu(message)
    elif num ==  "Двери":
        menudoors(message)
    elif num == ":55-":
        message.text = "ИСП-151/д"
        isp(message)
    elif num == "Рандом":
        games(message)
    elif num == "На главную":
        start(message)
    elif c == 2 and x == 1:
        a, b = ([int(i) for i in n])
        if a < b:
            say = tb.send_message(message.chat.id, f"Ваше число: " + str(random.randint(a, b)) + "\n\nЕще диапазоны?")
            tb.register_next_step_handler(say, randomer)
        else:
            say = tb.send_message(message.chat.id, f"Напиши нормально!")
            tb.register_next_step_handler(say, randomer)
    else:
        tb.send_message(message.chat.id, f"Неверный формат.")
        listgames(message)


def groups(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    isp111 = types.KeyboardButton('ИСП-111')
    isp111d = types.KeyboardButton('ИСП-111д')
    isp131 = types.KeyboardButton('ИСП-131/д')
    isp151 = types.KeyboardButton('ИСП-151/д')
    isp171 = types.KeyboardButton('ИСП-171/д')
    isp191d = types.KeyboardButton('ИСП-191д')
    back = types.KeyboardButton('На главную')
    markup1.add(isp111, isp111d, isp131, isp151, isp171, isp191d, back)
    say = tb.send_message(message.chat.id, f"""Выбери свою группу: \n(/д = совмещенная)""", reply_markup=markup1)
    tb.register_next_step_handler(say, isp)

def teachlist(message):
    markup13 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    eal = types.KeyboardButton('Елена Алексеевна')
    back = types.KeyboardButton('На главную')
    markup13.add(eal, back)
    say = tb.send_message(message.chat.id, f"""Выберите преподавателя:""", reply_markup=markup13)
    tb.register_next_step_handler(say, teachpars)


def isp(message):
    group = message.text
    if group == 'На главную':
        start(message)
    elif group in ['ИСП-111', 'ИСП-111д', 'ИСП-131/д', 'ИСП-151/д', 'ИСП-171/д', 'ИСП-191д']:
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        time = types.KeyboardButton("Звонки")
        study = types.KeyboardButton("Расписание пар")
        teacher = types.KeyboardButton("Преподаватели")
        back = types.KeyboardButton('На главную')
        markup2.add(time, study, teacher, back)
        say = tb.send_message(message.chat.id, f"Информация по группе {group}", reply_markup=markup2)
        tb.register_next_step_handler(say, action, group)
        loggy(message.chat.id, message.from_user.first_name, message.from_user.username, message.text)
    else:
        tb.send_message(message.chat.id, f"Я не знаю такой группы, либо она не добавлена...")
        groups(message)


def teachpars(message):
    week = int((datetime.now() + timedelta(hours=3)).strftime('%W'))
    txt = message.text
    if week % 2 != 0:
        name_week = 'нечётная'
        eal, eal_2, eal_3 = "История (111д)", "История (151/д)", ""
    if week % 2 == 0:
        name_week = 'чётная'
        eal, eal_2, eal_3 = "Родная лит-ра (171/д)", "Родная лит-ра (151/д)", ""
    if txt == "Елена Алексеевна":
        say = tb.send_message(message.chat.id,
        f"""<b>Пары:
week = ({name_week})</b>

    <i>----- Понедельник -----</i>
     0. Классный час (151/д)
     1. История (151/д)
     2. История ОГСЭ (121/д)
     3. Лит-ра (171/д)
     4. {eal}
    <i>----- Вторник -----</i>
     1. История (121/д)
     2. Лит-ра (111д)
     3. Лит-ра (151д)
     4. {eal_2}
    <i>----- Среда -----</i>
     В другом отделении.
    <i>----- Четверг -----</i>
     1. Менедж. в проф. д. (321)
     2. Менедж. в проф. д. (321)
     3. История (СА)
     4. История (СА)
    <i>----- Пятница -----</i>
     1. Менедж. в проф. д. (411д)
     2. Менедж. в проф. д. (411д)
     3. Менедж. в проф. д. (411)
     4. Менедж. в проф. д. (411)""", parse_mode="html")
        tb.register_next_step_handler(say, teachpars)
    elif txt == "На главную":
        start(message)
    else:
        say = tb.send_message(message.chat.id, f"Ничего не понял, попробуй еще раз.")
        tb.register_next_step_handler(say, teachpars)




def action(message, group='12'):
    week = int((datetime.now() + timedelta(hours=3)).strftime('%W'))
    act = message.text
    if week % 2 != 0:
        name_week = 'нечётная'
        i111, i111_2, i111_3 = "Родная лит-ра", "История", "Физ-ра"
        i111d, i111d_2, i111d_3, i111d_4 = "4. Родная лит-ра", "", "РПЗ", "Физ-ра"
        i131, i131_2, i131_3 = "РПЗ", "Родная лит-ра", "Инглиш"
        i151, i151_2, i151_3 = "История", "РПЗ", "Физ-ра"
        i171, i171_2, i171_3 = "", "История", "Инглиш"
        i191d, i191d_2, i191d_3 = "Родная лит-ра", "История", "Физ-ра"
    if week % 2 == 0:
        name_week = 'чётная'
        i111, i111_2, i111_3 = "Русский", "РПЗ", "Инглиш"
        i111d, i111d_2, i111d_3, i111d_4 = "", "4. Русский", "История", "Инглиш"
        i131, i131_2, i131_3 = "История", "Русский", "Физ-ра"
        i151, i151_2, i151_3 = "Родная лит-ра", "Русский", "Инглиш"
        i171, i171_2, i171_3 = "4. Родная лит-ра", "РПЗ", "Физ-ра"
        i191d, i191d_2, i191d_3 = "Русский", "РПЗ", "Инглиш"
    if act == "Звонки":
        bell(message, group)
    elif group == "ИСП-111":
        if act == "Расписание пар":
            say = tb.send_message(message.chat.id,
            f"""<b>Пары:
week = ({name_week})</b>

            <i>----- Понедельник -----</i>
             0. Классный час
             1. Инглиш
             2. Математика
             3. Русский
            <i>----- Вторник -----</i>
             1. Физика
             2. История
             3. Астрономия
             4. Математика
            <i>----- Среда -----</i>
             1. {i111}
             2. Информатика
             3. Математика
             4. {i111_2}
            <i>----- Четверг -----</i>
             1. Лит-ра
             2. Физ-ра
             3. Информатика
            <i>----- Пятница -----</i>
             1. {i111_3}
             2. Физика
             3. РПЗ
             4. ОБЖ""", parse_mode="html")
            tb.register_next_step_handler(say, action, group="ИСП-111")
        elif message.text == "Преподаватели":
            say = tb.send_message(message.chat.id, """Ведущие преподаватели:

<i>Куратор:</i> Ирина Николаевна

<i>Математика:</i> Елена Анатольевна
<i>Русский:</i> Елена Борисовна
<i>Родная лит-ра/Лит-ра:</i> Елена Борисовна
<i>Физ-ра:</i> Алексей Александрович
<i>Физика/Астрономия:</i> Ирина Николаевна
<i>Инглиш:</i> Светлана Витальевна
<i>История:</i> Людмила Сергеевна
<i>Информатика:</i> Али Балабекович
<i>РПЗ:</i> Алла Игоревна
<i>ОБЖ:</i> Владимир Владимирович""", parse_mode="html")
            tb.register_next_step_handler(say, action, group="ИСП-111")
        elif message.text == "На главную":
            groups(message)
        else:
            say = tb.send_message(message.chat.id, f"Ничего не понял, попробуй еще раз.")
            tb.register_next_step_handler(say, action, group="ИСП-111")
    elif group == "ИСП-111д":
        if act == "Расписание пар":
            say = tb.send_message(message.chat.id,
            f"""<b>Пары:
week = ({name_week})</b>

            <i>----- Понедельник -----</i>
             0. Классный час
             1. Русский
             2. Информатика
             3. Физика
             {i111d}
            <i>----- Вторник -----</i>
             1. Физ-ра
             2. Лит-ра
             3. Математика
             {i111d_2}
            <i>----- Среда -----</i>
             1. {i111d_3}
             2. Физика
             3. Математика
             4. Информатика
            <i>----- Четверг -----</i>
             1. ОБЖ
             2. История
             3. Инглиш
             4. Астрономия
            <i>----- Пятница -----</i>
             1. Математика
             2. РПЗ
             3. {i111d_4}""", parse_mode="html")
            tb.register_next_step_handler(say, action, group="ИСП-111д")
        elif message.text == "Преподаватели":
            say = tb.send_message(message.chat.id, """Ведущие преподаватели:

<i>Куратор: Мария Владимировна</i>

<i>Математика:</i> Алла Игоревна
<i>Русский:</i> Елена Борисовна
<i>Родная лит-ра/Лит-ра:</i> Елена Алексеевна
<i>Физика/Астрономия:</i> Ирина Николаевна
<i>Физ-ра:</i> Алексей Александрович
<i>Инглиш:</i> Светлана Витальевна
<i>История:</i> Людмила Сергеевна
<i>Информатика:</i> Али Балабекович
<i>РПЗ:</i> Алла Игоревна
<i>ОБЖ:</i> Владимир Владимирович""", parse_mode="html")
            tb.register_next_step_handler(say, action, group="ИСП-111д")
        elif act == "На главную":
            groups(message)
        else:
            say = tb.send_message(message.chat.id, f"Ничего не понял, попробуй еще раз.")
            tb.register_next_step_handler(say, action, group="ИСП-111д")
    elif group == "ИСП-131/д":
        if act == "Расписание пар":
            say = tb.send_message(message.chat.id,
            f"""<b>Пары:
week = ({name_week})</b>

            <i>----- Понедельник -----</i>
             0. Классный час
             1. Информатика
             2. Физика
             3. Математика
             4. Русский
            <i>----- Вторник -----</i>
             1. {i131}
             2. РПЗ
             3. Математика
             4. Астрономия
            <i>----- Среда -----</i>
             1. Математика
             2. {i131_2}
             3. Информатика
            <i>----- Четверг -----</i>
             1. История
             2. Лит-ра
             3. Инглиш
             4. Физ-ра
            <i>----- Пятница -----</i>
             1. Физика
             2. ОБЖ
             3. {i131_3}""", parse_mode="html")
            tb.register_next_step_handler(say, action, group="ИСП-131/д")
        elif message.text == "Преподаватели":
            say = tb.send_message(message.chat.id, """Ведущие преподаватели:

<i>Куратор: Елена Анатольевна</i>

<i>Математика:</i> Елена Анатольевна
<i>Русский:</i> Елена Борисовна
<i>Родная лит-ра/Лит-ра:</i> Елена Борисовна
<i>Физика/Астрономия:</i> Ирина Николаевна
<i>Физ-ра:</i> Вараздат Ашотович
<i>Инглиш:</i> Марина Геннадьевна
<i>История:</i> Людмила Сергеевна
<i>Информатика:</i> Али Балабекович
<i>РПЗ:</i> Алла Игоревна
<i>ОБЖ:</i> Владимир Владимирович""", parse_mode="html")
            tb.register_next_step_handler(say, action, group="ИСП-131/д")
        elif act == "На главную":
            groups(message)
        else:
            say = tb.send_message(message.chat.id, f"Ничего не понял, попробуй еще раз.")
            tb.register_next_step_handler(say, action, group="ИСП-131/д")
    elif group == "ИСП-151/д":
        if act == "Расписание пар":
            say = tb.send_message(message.chat.id,
            f"""<b>Пары:
week = ({name_week})</b>

            <i>----- Понедельник -----</i>
             0. Классный час
             1. История
             2. Русский
             3. Информатика
             4. Математика
            <i>----- Вторник -----</i>
             1. Математика
             2. Математика
             3. Лит-ра
             4. {i151}
            <i>----- Среда -----</i>
             1. Информатика
             2. РПЗ
             3. Физика
             4. {i151_2}
            <i>----- Четверг -----</i>
             1. Физ-ра
             2. Инглиш
             3. Астрономия
            <i>----- Пятница -----</i>
             1. ОБЖ
             2. {i151_3}
             3. Физика""", parse_mode="html")
            tb.register_next_step_handler(say, action, group="ИСП-151/д")
        elif message.text == "Преподаватели":
            say = tb.send_message(message.chat.id, """Ведущие преподаватели:

<i>Куратор: Елена Алексеевна</i>

<i>Математика:</i> Татьяна Владимировна
<i>Русский:</i> Елена Борисовна
<i>Родная лит-ра/Лит-ра:</i> Елена Алексеевна
<i>История:</i> Елена Алексеевна
<i>Физика/Астрономия:</i> Ирина Николаевна
<i>Физ-ра:</i> Алексей Александрович
<i>Инглиш:</i> Светлана Витальевна
<i>Информатика:</i> Али Балабекович
<i>РПЗ:</i> Алла Игоревна
<i>ОБЖ:</i> Владимир Владимирович""", parse_mode="html")
            tb.register_next_step_handler(say, action, group="ИСП-151/д")
        elif act == "На главную":
            groups(message)
        else:
            say = tb.send_message(message.chat.id, f"Ничего не понял, попробуй еще раз.")
            tb.register_next_step_handler(say, action, group="ИСП-151/д")
    elif group == "ИСП-171/д":
        if act == "Расписание пар":
            say = tb.send_message(message.chat.id,
            f"""<b>Пары:
week = ({name_week})</b>

            <i>----- Понедельник -----</i>
             0. Классный час
             1. Инглиш
             2. Математика
             3. Лит-ра
             {i171}
            <i>----- Вторник -----</i>
             1. {i171_2}
             2. Физика
             3. Математика
            <i>----- Среда -----</i>
             1. Физика
             2. История
             3. Русский
             4. Русский
            <i>----- Четверг -----</i>
             1. Астрономия
             2. Информатика
             3. Физ-ра
             4. Информатика
            <i>----- Пятница -----</i>
             1. Математика
             2. {i171_3}
             3. ОБЖ
             4. РПЗ""", parse_mode="html")
            tb.register_next_step_handler(say, action, group="ИСП-171/д")
        elif message.text == "Преподаватели":
            say = tb.send_message(message.chat.id, """Ведущие преподаватели:

<i>Куратор: Алла Игоревна</i>

<i>Математика:</i> Татьяна Владимировна
<i>Русский:</i> Елена Борисовна
<i>Родная лит-ра/Лит-ра:</i> Елена Алексеевна
<i>Физика/Астрономия:</i> Ирина Николаевна
<i>Физ-ра:</i> Вараздат Ашотович
<i>Инглиш:</i> Марина Геннадьевна
<i>История:</i> Людмила Сергеевна
<i>Информатика:</i> Али Балабекович
<i>РПЗ:</i> Алла Игоревна
<i>ОБЖ:</i> Владимир Владимирович""", parse_mode="html")
            tb.register_next_step_handler(say, action, group="ИСП-171/д")
        elif act == "На главную":
            groups(message)
        else:
            say = tb.send_message(message.chat.id, f"Ничего не понял, попробуй еще раз.")
            tb.register_next_step_handler(say, action, group="ИСП-171/д")
    elif group == "ИСП-191д":
        if act == "Расписание пар":
            say = tb.send_message(message.chat.id,
            f"""<b>Пары:
week = ({name_week})</b>

            <i>----- Понедельник -----</i>
             0. Классный час
             1. Инглиш
             2. Математика
             3. Русский
            <i>----- Вторник -----</i>
             1. Физика
             2. История
             3. Астрономия
             4. Математика
            <i>----- Среда -----</i>
             1. {i191d}
             2. Информатика
             3. Математика
             4. {i191d_2}
            <i>----- Четверг -----</i>
             1. Лит-ра
             2. Физ-ра
             3. Информатика
            <i>----- Пятница -----</i>
             1. {i191d_3}
             2. Физика
             3. РПЗ
             4. ОБЖ""", parse_mode="html")
            tb.register_next_step_handler(say, action, group="ИСП-191д")
        elif message.text == "Преподаватели":
            say = tb.send_message(message.chat.id, """Ведущие преподаватели:

<i>Куратор: Ирина Николаевна</i>

<i>Математика:</i> Елена Анатольевна
<i>Русский:</i> Елена Борисовна
<i>Родная лит-ра/Лит-ра:</i> Елена Борисовна
<i>Физика/Астрономия:</i> Ирина Николаевна
<i>Физ-ра:</i> Алексей Александрович
<i>Инглиш:</i> Светлана Витальевна
<i>История:</i> Людмила Сергеевна
<i>Информатика:</i> Али Балабекович
<i>РПЗ:</i> Алла Игоревна
<i>ОБЖ:</i> Владимир Владимирович""", parse_mode="html")
            tb.register_next_step_handler(say, action)
        elif act == "На главную":
            groups(message)
        else:
            say = tb.send_message(message.chat.id, f"Ничего не понял, попробуй еще раз.")
            tb.register_next_step_handler(say, action, group="ИСП-191д")
    else:
        say = tb.send_message(message.chat.id, f"Данная группа еще не добавлена, как вы сюда попали?.")
        tb.register_next_step_handler(say, groups, group="ИСП-191д")


def bell(message, group):
    say = tb.send_message(message.chat.id, """<b>Расписание звонков:</b>
    <b>  Понедельник</b>
        9:00 - 9:45
                -----
        9:55 - 10:40
        11:00 - 11:45
                -----
        12:05 - 12:50
        13:10 - 13:55
                -----
        14:15 - 15:45
                -----
        15:55 - 17:25
       ------------------------
    <b>         Вт-Пт </b>
        9:00 - 10:30
                -----
        10:50 - 11:35
        11:55 - 12:40
                -----
        13:00 - 13:45
        14:05 - 14:50
                -----
        15:00 - 16:30
                -----
        16:40 - 18:10""", parse_mode="html")
    tb.register_next_step_handler(say, action, group)


@tb.message_handler(content_types='text')
def prestart(message):
    tb.send_message(message.chat.id, f"Я был перезагружен, воспользуйся /start")


tb.polling(none_stop=True)