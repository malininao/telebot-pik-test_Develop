'''
def w(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    itembtn1 = types.KeyboardButton('Общие')
    itembtn2 = types.KeyboardButton('Конструкторы')
    itembtn3 = types.KeyboardButton('Архитекторы')
    itembtn4 = types.KeyboardButton('Инженеры ОВ')
    itembtn5 = types.KeyboardButton('Инженеры ВК')
    itembtn6 = types.KeyboardButton('Инженеры ЭОМ')
    itembtn7 = types.KeyboardButton('Инженеры СС')
    itembtn8 = types.KeyboardButton('Наружные сети')
    itembtn9 = types.KeyboardButton('ПОС')
    itembtn10 = types.KeyboardButton('НАЗАД')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10)
    msg = bot.send_message(message.chat.id,
                           'Привет, ' + message.from_user.first_name + ',выбери кнопку и нажми её!',
                           reply_markup=markup)
    bot.register_next_step_handler(msg, process_select_step1)


def process_select_step1(message):
    try:
        if (message.text == 'Общие'):
            w1(message)
        elif (message.text == 'Конструкторы'):
            w2(message)
        elif (message.text == 'Архитекторы'):
            w3(message)
        elif (message.text == 'Инженеры ОВ'):
           w4(message)
        elif (message.text == 'Инженеры ВК'):
             w5(message)
        elif (message.text == 'Инженеры ЭОМ'):
           w6(message)
        elif (message.text == 'Инженеры СС'):
           w6(message)
        elif (message.text == 'Наружные сети'):
           w7(message)
        elif (message.text == 'ПОС'):
           w8(message)
        elif (message.text == 'НАЗАД'):
           start(message)
        else:
            start(message)
    except Exception as e:
        bot.reply_to(message, 'Error 404')

def w1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('НАЗАД')
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, process_select555_step)

def process_select555_step(message):
    try:
        if (message.text == 'НАЗАД'):
                w(message)
        else:
                start(message)
    except Exception as e:
        bot.reply_to(message, 'Error 404')

def w1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('НАЗАД')
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, process_select555_step)

def w2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('НАЗАД')
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, process_select555_step)

def w3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('НАЗАД')
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, process_select555_step)

def w4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('НАЗАД')
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, process_select555_step)

def w5(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('НАЗАД')
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, process_select555_step)

def w6(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('НАЗАД')
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, process_select555_step)

def w7(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('НАЗАД')
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, process_select555_step)

def w8(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('НАЗАД')
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, process_select555_step)



def po111(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('Появляется предупреждение')
    itembtn2 = types.KeyboardButton('Файл тормозит')
    itembtn3 = types.KeyboardButton('Файл вылетает с фатальной ошибкой')
    itembtn4 = types.KeyboardButton('Не отображается')
    itembtn5 = types.KeyboardButton('Не срабатывает команда')
    itembtn6 = types.KeyboardButton('Неккоректно срабатывает команда')
    itembtn7 = types.KeyboardButton('Установка дополнительных плагинов')
    itembtn8 = types.KeyboardButton('Неккоректная печать')
    itembtn9 = types.KeyboardButton("Вернуться в 'Помощь в работе'")
    markup.add(itembtn1, itembtn2 ,itembtn3 , itembtn4, itembtn5, itembtn6, itembtn7 , itembtn8, itembtn9)
    msg=bot.send_message(message.chat.id,'какая проблема', reply_markup=markup)
    bot.register_next_step_handler(msg, l)

def l(message):
    try:
        if (message.text == "Вернуться в 'Помощь в работе'"):
            po_main(message)
        elif (message.text == 'Появляется предупреждение'):
            po11(message)
        elif (message.text == 'Файл тормозит'):
           po12(message)
        elif (message.text == 'Файл вылетает с фатальной ошибкой'):
           po13(message)
        elif (message.text == 'Не отображается'):
           po14(message)
        elif (message.text == 'Не срабатывает команда'):
           po15(message)
        elif (message.text == 'Неккоректно срабатывает команда'):
           po16(message)
        elif (message.text == 'Установка дополнительных плагинов'):
           po17(message)
        elif (message.text == 'Неккоректная печать'):
           po18(message)

        else:
            start(message)
    except Exception as e:
        bot.reply_to(message, 'Error 404')

def po12(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, l1)
def l1(message):
    try:
        if (message.text == "НАЗАД"):
            po111(message)
        else:
            start(message)
    except Exception as e:
        bot.reply_to(message, 'Error 404')
def po11(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = types.KeyboardButton("1.Невозможно открыть файл чертежа, так как он создан в более поздней версии AutoCAD")
    itembtn2 = types.KeyboardButton("2.Отсутствует один или несколько файлов SHX. Выберите требуемое действие")
    itembtn3 = types.KeyboardButton("3.Программа 'AutoCAD Application' не работает")
    itembtn4 = types.KeyboardButton("4.Не удаётся прочитать пользовательский словарь")
    itembtn5 = types.KeyboardButton("5.Эта версия AutoCAD не поддерживается. поддерживаемые версии AutoCAD 2010- AutoCAD 2018")
    itembtn6 = types.KeyboardButton("6.Копирование в буфер не выполнено")
    itembtn7 = types.KeyboardButton('7.Файл сейчас используется или имеет атрибут "только для чтения"')
    itembtn8 = types.KeyboardButton("8.ФАТАЛЬНАЯ ОШИБКА: Unhandled e0434352h Exception at B79CA839h")
    itembtn9 = types.KeyboardButton("9.Microsoft Excel ожидает, пока другое приложение завершит действие OLE")
    itembtn10 = types.KeyboardButton("10.Не удалось загрузить файл профиля. Некоторые данные профиля, сохраненные в последнем сеансе, возможно, не будут восстановлены")
    itembtn11 = types.KeyboardButton("11.Один или несколько объектов на чертеже невозможно сохранить в указанном формате при сохранении файла в AutoCAD")
    itembtn12 = types.KeyboardButton("12.Мне не помог ни один из предложенных вариантов")
    itembtn13 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1,itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10, itembtn11, itembtn12, itembtn13)
    msg=bot.send_message(message.chat.id,'Выберете ошибку', reply_markup=markup)
    bot.register_next_step_handler(msg, m111)

def m111(message):
    try:
        if (message.text == "НАЗАД"):
            po111(message)
        elif (message.text == '1.Невозможно открыть файл чертежа, так как он создан в более поздней версии AutoCAD'):
            m(message)
        elif (message.text == '2.Отсутствует один или несколько файлов SHX. Выберите требуемое действие'):
             m1(message)
        elif (message.text == '3.Программа "AutoCAD Application" не работает'):
             m2(message)
        elif (message.text == '4.Не удаётся прочитать пользовательский словарь'):
              m3(message)
        elif (message.text == '5.Эта версия AutoCAD не поддерживается. поддерживаемые версии AutoCAD 2010- AutoCAD 2018'):
              m4(message)
        elif (message.text == '6.Копирование в буфер не выполнено'):
              m5(message)
        elif (message.text == '7.Файл сейчас используется или имеет атрибут "только для чтения"'):
              m6(message)
        elif (message.text == '8.ФАТАЛЬНАЯ ОШИБКА: Unhandled e0434352h Exception at B79CA839h'):
              m7(message)
        elif (message.text == '9.Microsoft Excel ожидает, пока другое приложение завершит действие OLE'):
              m8(message)
        elif (message.text == '10.Не удалось загрузить файл профиля. Некоторые данные профиля, сохраненные в последнем сеансе, возможно, не будут восстановлены'):
              m9(message)
        elif (message.text == '11.Один или несколько объектов на чертеже невозможно сохранить в указанном формате при сохранении файла в AutoCAD'):
              m10(message)
        elif (message.text == '12.Мне не помог ни один из предложенных вариантов'):
              m11(message)

        else:
            start(message)
    except Exception as e:
        bot.reply_to(message, 'Error 404')

#для того чтобы сделать жирный текст поставь *а здесь свой теккст* если надо только одну часть или кусочек текста то разрываешь ковычки ставишь + и открываешь новые  \n - это командп начинает текст сновой строчки
def m(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id, "\n*Жирный шрифт*" + "еще текст",parse_mode="MARKDOWN", reply_markup=markup)
    bot.register_next_step_handler(msg, tt1)
def tt1(message):
    try:
        if (message.text == "НАЗАД"):
            po11(message)
        else:
            start(message)
    except Exception as e:
        bot.reply_to(message, 'Error 404')

def m1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, tt1)

def m2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, tt1)

def m3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, tt1)

def m4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, tt1)

def m5(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, tt1)

def m6(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, tt1)

def m7(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, tt1)

def m8(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, tt1)

def m9(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, tt1)

def m10(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'Причина\nПрограмма не распознает прокси-объекты\nРешение\nВариант 1\nПрименить команду PIK_OPTIMIZATION\nВариант 2\nПрименить команду _audit\nВариант 3\nВключить распознавание прокси-объектов, установив значение 1 для следующих переменных:\nPROXYGRAPHICS: сохраняется в чертеже (исходное значение 1)\nPROXYNOTICE: сохраняется в реестре (исходное значение 1)\nPROXYSHOW: сохраняется в реестре (исходное значение 1)\nЗатем использовать команду EXPORTTOAUTOCAD для создания файла, который включает только собственные объекты AutoCAD.\nВариант 4\nСкопировать содержимое поврежденного файла в новый.\nВариант 5\nЕсли используется vdi соединение, необходимо перезагрузить виртуальную машину', reply_markup=markup)
    bot.register_next_step_handler(msg, tt1)

def m11(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, tt1)

def m12(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, tt1)






def po13(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, l1)
def po14(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, l1)
def po15(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, l1)
def po16(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, l1)
def po17(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, l1)
def po18(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)
    bot.register_next_step_handler(msg, l1)


def po1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)



def po2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)



def po3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton("НАЗАД")
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'ваш текст', reply_markup=markup)








def q1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('ВЕРНУТЬСЯ В МЕНЮ')
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'текст к кнопки 1', reply_markup=markup)
    bot.register_next_step_handler(msg, process_select55_step)

def q2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('ВЕРНУТЬСЯ В МЕНЮ')
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'текст к кнопки 2', reply_markup=markup)
    bot.register_next_step_handler(msg, process_select55_step)

def q3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('ВЕРНУТЬСЯ В МЕНЮ')
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'текст к кнопки 3', reply_markup=markup)
    bot.register_next_step_handler(msg, process_select55_step)

def q4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('ВЕРНУТЬСЯ В МЕНЮ')
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'текст к кнопки 4', reply_markup=markup)
    bot.register_next_step_handler(msg, process_select55_step)

def q5(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('ВЕРНУТЬСЯ В МЕНЮ')
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'текст к кнопки 5', reply_markup=markup)
    bot.register_next_step_handler(msg, process_select55_step)

def q6(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('ВЕРНУТЬСЯ В МЕНЮ')
    markup.add(itembtn1)
    msg=bot.send_message(message.chat.id,'текст к кнопки 6', reply_markup=markup)
    bot.register_next_step_handler(msg, process_select55_step)

def process_select55_step(message):
    try:
        if (message.text == 'ВЕРНУТЬСЯ В МЕНЮ'):
            service_select_step(message)
        else:
            service_select_step(message)
    except Exception as e:
        bot.reply_to(message, 'Error 404')


@bot.message_handler(commands=['q'])
def lol(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Сюда можно вставить любую ссылку', url='https://t.me/Osipiya_bot')
    markup.add(btn_my_site)
    msg=bot.send_message(message.chat.id, "Возможно эта функция вам понадабиться(сейчас эта кнопка кидает на этого бота)", reply_markup=markup)
    bot.register_next_step_handler(msg, start)

import telebot
from telebot import types
import telebot
from telebot.types import Message
from config import TOKEN
from mainDataBase import getData

#не забуд прописать в терминал команду pip install pytelegrambotapi (если у тебя мак то pip3, а не pip)

bot = telebot.TeleBot(TOKEN)
#Подключаем данные из БД
'''
services = getData('services')
programs = getData('program')
'''
data = getData('services')

#это глвное меню бота (вызывается из базы данных, формируется на основе ее значений)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1) #переменная вызывает клавиатуру
    itembtn = types.KeyboardButton('СТАРТ')
    markup.add(itembtn)
    bot.send_message(message.chat.id,'Что может делать этот бот ?'+'\n'+''+'\n'
    'Бот помощник Osipia 👷 - Ваш персональный BIM - помощник.'+'\n'
    '🛠 Решение проблем в работе ПО.'+'\n'+
    '🔍 Навигация и поиск по учебным материалам.'+'\n'
    '📚 Полезные ссылки и материалы.')
    msg = bot.send_message(message.chat.id,
                           'Привет, ' + message.from_user.first_name + ', нажми СТАРТ',
                           reply_markup=markup) #вызвать клаву
    bot.register_next_step_handler(msg, main_menu_select_step)
#Пускай пока побудет тут, контролирую что выводится
#for item in services:
    #print(item[1])


def main_menu_select_step(message):
    ids = []
    nextStep = []
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # переменная вызывает клавиатуру
    for item in services:
        itembtn = types.KeyboardButton(item[1])
        markup.add(itembtn)
        ids.append(item[1])
        nextStep.append(item[2])
    itemBtnBack = types.KeyboardButton('В НАЧАЛО')
    markup.add(itemBtnBack)
    msg = bot.send_message(message.chat.id,
                           'Главное меню',
                           reply_markup=markup)  # вызвать клаву
    bot.register_next_step_handler(msg, process_select_step)

#логика довольно простая если кто то хоть раз что то писал то поймет этот код но если будут вопросы то пиши в телеге
def process_select_step(message):
    try:
        if (message.text == 'Помощь в работе'):
            po_main(message)
        elif (message.text == 'Новому сотруднику'):
            q2(message)
        elif (message.text == 'Фабрика семейств'):
            q3(message)
        elif (message.text == 'Помощь в работе'):
            po_main(message)
        elif (message.text == '5'):
            q5(message)
        elif (message.text == '6'):
            q6(message)
        elif (message.text == 'кнопка с ссылкой'):
            q7(message)
        else:
            main_menu_select_step(message)
    except Exception as e:
        bot.reply_to(message, 'Error 404')

def po_main(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # переменная вызывает клавиатуру
    for item in programs:
        itembtn = types.KeyboardButton(item[1])
        markup.add(itembtn)
        
    itemBtnBack = types.KeyboardButton('В НАЧАЛО')
    markup.add(itemBtnBack)
    msg = bot.send_message(message.chat.id,
                           'Выберите ПО',
                           reply_markup=markup)  # вызвать клаву
    bot.register_next_step_handler(msg, program_select_step)


def program_select_step(message):
    try:
        if (message.text == 'AutoCad/Civil'):
            po111(message)
        elif (message.text == 'Revit'):
            po111(message)
        elif (message.text == 'Другое'):
            po3(message)
        elif (message.text == 'На главную'):
            main_menu_select_step(message)
        else:
            start(message)
    except Exception as e:
        bot.reply_to(message, 'Error 404')





@bot.message_handler(func=lambda m: True)
def message(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет,друг!')
    elif message.text == 'hi':
        bot.send_message(message.chat.id, 'Hi again!')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'До свидания! Хорошего дня!)')
    elif message.text == 'Hi':
        bot.send_message(message.chat.id, 'Hi again! , ' + message.from_user.first_name + '!How are you?!')
    elif message.text == 'привет':
        bot.send_message(message.chat.id, 'ПРИВЕТ! , ' + message.from_user.first_name)

    else:
        start(message)





if __name__ == '__main__':
    bot.polling(none_stop=True)




12.02.2021
import telebot
from telebot import types
import telebot
from telebot.types import Message
from config import TOKEN
from mainDataBase import getData

#не забуд прописать в терминал команду pip install pytelegrambotapi (если у тебя мак то pip3, а не pip)

bot = telebot.TeleBot(TOKEN)
#Подключаем данные из БД

data = getData('services')

#это глвное меню бота (вызывается из базы данных, формируется на основе ее значений)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1) #переменная вызывает клавиатуру
    itembtn = types.KeyboardButton('СТАРТ')
    markup.add(itembtn)
    bot.send_message(message.chat.id,'Что может делать этот бот ?'+'\n'+''+'\n'
    'Бот помощник Osipia 👷 - Ваш персональный BIM - помощник.'+'\n'
    '🛠 Решение проблем в работе ПО.'+'\n'+
    '🔍 Навигация и поиск по учебным материалам.'+'\n'
    '📚 Полезные ссылки и материалы.')
    msg = bot.send_message(message.chat.id,
                           'Привет, ' + message.from_user.first_name + ', нажми СТАРТ',
                           reply_markup=markup) #вызвать клаву
    bot.register_next_step_handler(msg, start_bot)
#Пускай пока побудет тут, контролирую что выводится
#for item in services:
    #print(item[1])
def start_bot(message):
    if message.text == "СТАРТ":
        main_menu_select_step(message, data)

def main_menu_select_step(message, data):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # переменная вызывает клавиатуру
    for item in data:
        itembtn = types.KeyboardButton(item[1])
        markup.add(itembtn)
    msg = bot.send_message(message.chat.id,
                           'Главное меню',
                           reply_markup=markup)  # вызвать клаву
    bot.register_next_step_handler(msg, process_select_step, data)
#логика довольно простая если кто то хоть раз что то писал то поймет этот код но если будут вопросы то пиши в телеге

#Обработка исключений отключена так как нет четкой работы алгоритма запросов
def process_select_step(message, data):
    try:
        #ids = []
        nextStep = []
        texts = []

        #table = 'services'
        #data = getData(table)
        for item in data:
            #ids.append(item[0])
            texts.append(item[1])
            nextStep.append(str(item[2]))
            print(item[1],"->", item[2])
        if message.text == "В НАЧАЛО":
            main_menu_select_step(message, data)
        else:
            index = texts.index(message.text)
            table = nextStep[index]
            print(table)
            if table != "program":
                bot.send_message(message.chat.id, "Такого раздела временно нет")
                #table= 'services'
                #data = getData(table)
                #main_menu_select_step(message, data)
            elif table == "<-":
                main_menu_select_step(message,data)
            else:
                data = getData(table)
                second_menu_select_step(message, data)
    except Exception as e:
        bot.reply_to(message, 'Error 404')

def second_menu_select_step(message, data):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # переменная вызывает клавиатуру
    for item in data:
        itembtn = types.KeyboardButton(item[1])
        markup.add(itembtn)
    itemBtnBack = types.KeyboardButton('В НАЧАЛО')
    markup.add(itemBtnBack)
    msg = bot.send_message(message.chat.id,
                           'Выберите ПО',
                           reply_markup=markup)  # вызвать клаву
    bot.register_next_step_handler(msg, second_process_select_step)

def second_process_select_step(message):
    try:
        #ids = []
        nextStep = []
        texts = []
        table = 'program'
        data = getData(table)
        for item in data:
            #ids.append(item[0])
            texts.append(item[1])
            nextStep.append(str(item[2]))
            print(item[1],"->", item[2])
        if message.text == "В НАЧАЛО":
            data = getData('services')
            main_menu_select_step(message, data)
        else:
            index = texts.index(message.text)
            table = nextStep[index]
            if table == "-":
                bot.send_message(message.chat.id, "Такого раздела временно нет")
            elif table == "<-":
                data = getData('services')
                main_menu_select_step(message, data)
            else:
                data = getData(table)
                third_menu_select_step(message, data)
    except Exception as e:
        bot.reply_to(message, 'Error 404')


def third_menu_select_step(message, data):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # переменная вызывает клавиатуру
    for item in data:
        itembtn = types.KeyboardButton(item[1])
        markup.add(itembtn)
    itemBtnBack = types.KeyboardButton('В НАЧАЛО')
    markup.add(itemBtnBack)
    msg = bot.send_message(message.chat.id,
                           'Выберите ПО',
                           reply_markup=markup)  # вызвать клаву
    bot.register_next_step_handler(msg, third_process_select_step)

def third_process_select_step(message):
    try:
        #ids = []
        nextStep = []
        texts = []
        table = 'symptomsACadCivil'
        data = getData(table)
        for item in data:
            #ids.append(item[0])
            texts.append(item[1])
            nextStep.append(str(item[2]))
            print(item[1],"->", item[2])
        if message.text == "В НАЧАЛО":
            data = getData('services')
            main_menu_select_step(message, data)
        else:
            index = texts.index(message.text)
            table = nextStep[index]
            if table == "-":
                bot.send_message(message.chat.id, "Такого раздела временно нет")
            elif table == "<-":
                data = getData('program')
                second_menu_select_step(message, data)
            else:
                data = getData(table)
                fourth_menu_select_step(message, data)
    except Exception as e:
        bot.reply_to(message, 'Error 404')


def fourth_menu_select_step(message, data):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # переменная вызывает клавиатуру
    for item in data:
        itembtn = types.KeyboardButton(item[1])
        markup.add(itembtn)
    itemBtnBack = types.KeyboardButton('В НАЧАЛО')
    markup.add(itemBtnBack)
    msg = bot.send_message(message.chat.id,
                           'Выберите ПО',
                           reply_markup=markup)  # вызвать клаву
    bot.register_next_step_handler(msg, fourth_process_select_step)

def fourth_process_select_step(message):
    try:
        #ids = []
        nextStep = []
        texts = []
        table = 'symptomsACadCivil'
        data = getData(table)
        for item in data:
            #ids.append(item[0])
            texts.append(item[1])
            nextStep.append(str(item[2]))
            print(item[1],"->", item[2])
        if message.text == "В НАЧАЛО":
            data = getData('services')
            main_menu_select_step(message, data)
        else:
            index = texts.index(message.text)
            table = nextStep[index]
            if table == "-":
                bot.send_message(message.chat.id, "Такого раздела временно нет")
            elif table == "<-":
                data = getData('program')
                third_menu_select_step(message, data)
            else:
                data = getData(table)
                fiveth_menu_select_step(message, data)
    except Exception as e:
        bot.reply_to(message, 'Error 404')

def fiveth_menu_select_step(message, data):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # переменная вызывает клавиатуру
    for item in data:
        itembtn = types.KeyboardButton(item[1])
        markup.add(itembtn)
    itemBtnBack = types.KeyboardButton('В НАЧАЛО')
    markup.add(itemBtnBack)
    msg = bot.send_message(message.chat.id,
                           'Выберите ПО',
                           reply_markup=markup)  # вызвать клаву
    bot.register_next_step_handler(msg, fiveth_process_select_step)

def fiveth_process_select_step(message):
    try:
        #ids = []
        nextStep = []
        texts = []
        table = 'symptomsACadCivil'
        data = getData(table)
        for item in data:
            #ids.append(item[0])
            texts.append(item[1])
            nextStep.append(str(item[2]))
            print(item[1],"->", item[2])
        if message.text == "В НАЧАЛО":
            data = getData('services')
            main_menu_select_step(message, data)
        else:
            index = texts.index(message.text)
            table = nextStep[index]
            if table == "-":
                bot.send_message(message.chat.id, "Такого раздела временно нет")
            elif table == "<-":
                data = getData('program')
                third_menu_select_step(message, data)
            else:
                data = getData(table)
                fiveth_menu_select_step(message, data)
    except Exception as e:
        bot.reply_to(message, 'Error 404')


@bot.message_handler(func=lambda m: True)
def message(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет,друг!')
    elif message.text == 'hi':
        bot.send_message(message.chat.id, 'Hi again!')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'До свидания! Хорошего дня!)')
    elif message.text == 'Hi':
        bot.send_message(message.chat.id, 'Hi again! , ' + message.from_user.first_name + '!How are you?!')
    elif message.text == 'привет':
        bot.send_message(message.chat.id, 'ПРИВЕТ! , ' + message.from_user.first_name)

    else:
        start(message)

if __name__ == '__main__':
    bot.polling(none_stop=True)
   #if nextStep[index].count('t0')>0:
             #   table = nextStep[index]
              #  data=getData(table)
               # instructionList = []
                #for item in data:
                 #   instructionList.append(item[5])
                #index = texts.index(message.text)
                #instruction = instructionList[index]
                #print_instruction_step(message, instruction, data)
        #   else:
        
//11.03.2021
import telebot
from telebot import types
import telebot
from telebot.types import Message
from config import TOKEN
from data_functions import getData

#не забуд прописать в терминал команду pip install pytelegrambotapi (если у тебя мак то pip3, а не pip)

bot = telebot.TeleBot(TOKEN)
#Подключаем данные из БД

data = getData('t1')

#это глвное меню бота (вызывается из базы данных, формируется на основе ее значений)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1) #переменная вызывает клавиатуру
    itembtn = types.KeyboardButton('СТАРТ')
    markup.add(itembtn)
    bot.send_message(message.chat.id,'Что может делать этот бот ?'+'\n'+''+'\n'
    'Бот помощник Osipia 👷 - Ваш персональный BIM - помощник.'+'\n'
    '🛠 Решение проблем в работе ПО.'+'\n'+
    '🔍 Навигация и поиск по учебным материалам.'+'\n'
    '📚 Полезные ссылки и материалы.')
    msg = bot.send_message(message.chat.id,
                           'Привет, ' + message.from_user.first_name + ', нажми СТАРТ',
                           reply_markup=markup) #вызвать клаву
    bot.register_next_step_handler(msg, main_menu_select_step, data)


#функция заполняет клавиатуру которая генерируется из базы данных (только главное меню)
def main_menu_select_step(message, data):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # переменная вызывает клавиатуру
    messageList = []

    for item in data:
        itembtn = types.KeyboardButton(item[1])
        messageList.append(str(item[4]))
        markup.add(itembtn)
    msg = bot.send_message(message.chat.id,
                           messageList[0],
                           reply_markup=markup)  # вызвать клаву
    bot.register_next_step_handler(msg, process_select_step, data)


#выбор дальнейших шагов в по таблицам БД
def process_select_step(message, data):
    try:
        #пустые массивы в начале функций нужны для того что при каждом вызове функции из значения заполнялись заново
        nextStep = []
        texts = []
        lastStep = []
        firstTable = 't1'
        for item in data: #пробег по массиву из кортежей, получаем следующую т
            # аблицу, текст кнопок, и предыдущую таблицу

            texts.append(item[1])
            nextStep.append(str(item[2]))
            lastStep.append(str(item[3]))
            print(item[1],"->", item[2])

        index = texts.index(message.text)
        table = nextStep[index]
        lastTable = lastStep[index]

        print(str("t01" in nextStep))
        print(str("t02" in nextStep))
        if "t01" in nextStep or "t02" in nextStep or "t1" in nextStep: #если следующая таблица пустая то вызывается
            # функция в которой выводится текст инструкции

            instructionList=[]
            for item in data:
                instructionList.append(item[5])
            index = texts.index(message.text)
            instruction = instructionList[index]
            table = nextStep[index]
            if nextStep[index] == 't1':
                data = getData(table)
                print_instruction_whithout_solution_step(message, instruction, data)
            elif nextStep[index] == 't01' or nextStep[index] == 't02':
                data = getData(table)
                print_instruction_step(message, instruction, data)
            elif nextStep[index] == '<-':
                data = getData(lastTable)
                menu_select_step(message, data)
            else:
                data = getData(table)
                print_instruction_and_next_step(message, instruction, data)

        else:#в любом другом случае получаем данные о дальнейшем и предыдущем шаге
            # для вызова шаблонной функции генерации кнопок

            print(table)
            if table == "<-":
                data = getData(lastTable)
                menu_select_step(message, data)
            else:
                data = getData(table)
                menu_select_step(message, data)

    except Exception as e:
        if message.text == "В НАЧАЛО":
            data = getData(firstTable)
            main_menu_select_step(message, data)
        else:
            bot.reply_to(message, 'Такого раздела пока нет')
            #start(message)
            data=getData(firstTable)
            main_menu_select_step(message, data)


#Обычная функция генерации кнопок, ничего примечательного
def menu_select_step(message, data):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # переменная вызывает клавиатуру
    messageList = []
    for item in data:
        itembtn = types.KeyboardButton(item[1])
        messageList.append(str(item[4]))
        markup.add(itembtn)
    itemBtnBack = types.KeyboardButton('В НАЧАЛО')
    markup.add(itemBtnBack)
    msg = bot.send_message(message.chat.id,
                           messageList[0],
                           reply_markup=markup)  # вызвать клаву
    bot.register_next_step_handler(msg, process_select_step, data)

#функция отвечает за вывод текста(далее изображений) инструкции
def print_instruction_step(message, instruction, data):
    if instruction != "":
        bot.send_message(message.chat.id, instruction)
    data = data
    final_menu_select_step(message, data)

def print_instruction_and_next_step(message, instruction, data):
    if instruction != "":
        bot.send_message(message.chat.id, instruction)
    data = data
    menu_select_step(message, data)
#функция которая срабатывает при нажатии кнопки где нет инструкции
def print_instruction_whithout_solution_step(message, instruction, data):
    if instruction != "":
        bot.send_message(message.chat.id, instruction)
    data = data
    main_menu_select_step(message, data)

#Последний шаг, генерируются кнопки для завершения работы (вопрос: помогло или нет?)
def final_menu_select_step(message, data):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # переменная вызывает клавиатуру
    messageList = []
    for item in data:
        itembtn = types.KeyboardButton(item[1])
        messageList.append(str(item[2]))
        markup.add(itembtn)
    msg = bot.send_message(message.chat.id,
                           messageList[0],
                           reply_markup=markup)  # вызвать клаву
    bot.register_next_step_handler(msg, final_process_select_step, data)

#выводится тескт с дальнейшими указаниями если инструкция не помогла. (в дальнейшем здесь будет вызываться запись в БД)
def final_process_select_step(message, data):
    try:
        texts = []
        answers = []
        firstTable = 't1'
        for item in data:
            texts.append(item[1])
            answers.append(item[3])
        index = texts.index(message.text)
        bot.send_message(message.chat.id, answers[index])
        data = getData(firstTable)
        main_menu_select_step(message, data)
    except Exception as e:
        bot.reply_to(message, 'Error 405')
        start(message)



#Не знаю что это но без этого не работает
@bot.message_handler(func=lambda m: True)
def message(message):
        start(message)

if __name__ == '__main__':
    try:
        bot.polling(none_stop=True, interval=0)
    except:
        pass

def start(message):
    # Подключаем данные из БД
    data = getData('t1')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)  #переменная вызывает клавиатуру
    itembtn = types.KeyboardButton('СТАРТ')
    markup.add(itembtn)
    bot.send_message(message.chat.id,'Что может делать этот бот ?'+'\n'+''+'\n'
    'Бот помощник Osipia 👷 - Ваш персональный BIM - помощник.'+'\n'
    '🛠 Решение проблем в работе ПО.'+'\n'+
    '🔍 Навигация и поиск по учебным материалам.'+'\n'
    '📚 Полезные ссылки и материалы.', disable_notification=True)
    msg = bot.send_message(message.chat.id,
                           'Привет, ' + message.from_user.first_name + ', нажми СТАРТ',
                           reply_markup=markup, disable_notification=True) #вызвать клаву
    bot.register_next_step_handler(msg, main_menu_select_step, data)
    
    
    
    
    
    
    #cursor.execute("""DROP TABLE IF EXISTS services""")
    #Потом удалится, взаимодействие с базой через приложение DB Browser


    test = cursor.execute("""SELECT services.text, program.program_name FROM services INNER JOIN
    Program ON services.id = program.service_id
    WHERE service_id=1;
    """)
    for item in test:
        print(item)
        
        
        
def getSelectedData(firstData, secondData, id):
    test = cursor.execute(f"""SELECT {firstData}.text, {secondData}.program_name FROM services INNER JOIN
      Program ON {firstData}.id = {secondData}.syptoms_id
      WHERE syptoms_id={id};
      """)
    return
'''