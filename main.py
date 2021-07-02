import datetime
import logging
import os
import secrets
import string

import telebot
from telebot import types

from data_functions import getData
from google_module import GoogleDocs, GoogleDocsRead, GoogleSheets
from recode_instriction_name import DecoderTableName

logger = telebot.logger


def dict_from_string(dict_in_string):
    first_list = str(dict_in_string).split(',')
    second_list = [tuple(str(item).split(':')) for item in first_list]
    third_list = [(key.replace(' ', '', 1), value.replace(' ','',1)) for key, value in second_list]
    dictionary = {key: value for key, value in third_list}
    return dictionary

HEROKU = os.environ.get('HEROKU')
if HEROKU == "True":
    TOKEN = os.environ.get('TOKEN')
    LINK_URL_SHEET = os.environ.get('LINK_URL_SHEET')
    KEY_USER_PARAM = os.environ.get('KEY_USER_PARAM')
    USER_BASE = os.environ.get('USER_BASE')
    KEY_INSTRUCT_PARAM = os.environ.get('KEY_INSTRUCT_PARAM')
    REQUEST_BASE = os.environ.get('REQUEST_BASE')
    DICTIONARY_INSTRUCT_REQUEST = dict_from_string(os.environ.get('DICTIONARY_INSTRUCT_REQUEST'))
    DICTIONARY_USER_REQUEST = dict_from_string(os.environ.get('DICTIONARY_USER_REQUEST'))
else:
    import config
    TOKEN = config.TOKEN
    LINK_URL_SHEET = config.LINK_URL_SHEETS
    KEY_USER_PARAM = config.KEY_USER_PARAM
    USER_BASE = config.USER_BASE
    KEY_INSTRUCT_PARAM = config.KEY_INSTRUCT_PARAM
    REQUEST_BASE = config.REQUEST_BASE
    DICTIONARY_INSTRUCT_REQUEST = dict_from_string(config.DICTIONARY_INSTRUCT_REQUEST)
    DICTIONARY_USER_REQUEST = dict_from_string(config.DICTIONARY_USER_REQUEST)

sheet_data = GoogleSheets(LINK_URL_SHEET)
bot = telebot.TeleBot(TOKEN)


# это глвное меню бота (вызывается из базы данных, формируется на основе ее значений)
# функция заполняет клавиатуру которая генерируется из базы данных (только главное меню)
# telebot.logger.setLevel(logging.DEBUG)

def get_date_time():
    offset = datetime.timedelta(hours=3)
    dt = datetime.datetime.now(tz=datetime.timezone(offset, 'МСК'))
    date = f'{dt.date().day}.{dt.date().month}.{dt.date().year}'
    time = f'{dt.time().hour}:{dt.time().minute}:{dt.time().second}'
    return date, time


def get_instruction_token(length):
    letters_and_digits = string.ascii_letters + string.digits
    instriction_token = ''.join(secrets.choice(
        letters_and_digits) for i in range(length))
    print("ID обращения", length, "символов:", instriction_token)
    return instriction_token


@bot.message_handler(commands=['start'])
def start(message):

    set_job_email(message)


@bot.message_handler(content_types=['text'])
def reload_bot(message):
    set_job_email(message)


def set_job_email(message):

    sheet_values = sheet_data.get_sheets_values_from_base(USER_BASE, start_column='A',
                                                          start_row='2', end_column='C')
    dictionary = sheet_data.get_dict(sheet_values, DICTIONARY_USER_REQUEST)
    user_data = sheet_data.get_data_from_base(message.chat.id, dictionary, KEY_USER_PARAM)

    if user_data[0] == "Данных нет в базе":
        markup = types.ReplyKeyboardRemove()
        msg = bot.send_message(message.chat.id, "Введите рабочую почту", reply_markup=markup, disable_notification=True)

        bot.register_next_step_handler(msg, add_user_in_base, user_data, sheet_values)

    else:
        main_menu_select_step(message)


def add_user_in_base(message, user_data, sheet_values):
    if "@pik.ru" in message.text:
        bot.send_message(message.chat.id, "Данные записываются...")
        sheet_data.add_user_in_base(user_data, message.chat.id, message.chat.username,
                                    "База пользователей", message.text, sheet_values)
        telebot.logger.setLevel(logging.DEBUG)
        main_menu_select_step(message)
    else:
        bot.send_message(message.chat.id, "Почта не зарегистрирована в домене pik.ru")
        set_job_email(message)


def main_menu_select_step(message):
    instruction_token = get_instruction_token(16)
    data = getData('t1')
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    message_list = []
    for item in data:
        if item[1] != "" and item[2] is not None and item[2] != "":

            item_btn = types.KeyboardButton(item[1])
            markup.add(item_btn)
        message_list.append(str(item[4]))
    msg = bot.send_message(message.chat.id,
                           message_list[0],
                           reply_markup=markup, disable_notification=True)  # вызвать клаву
    bot.register_next_step_handler(msg, process_select_step, data, 't1', instruction_token)


# выбор дальнейших шагов в по таблицам БД
def process_select_step(message, data, selected_table, instruction_token):
    # пустые массивы в начале функций нужны для того что при каждом вызове функции из значения заполнялись заново
    next_step = []
    texts = []
    last_step = []

    try:
        for item in data:  # пробег по массиву из кортежей, получаем следующую т
            # аблицу, текст кнопок, и предыдущую таблицу
            texts.append(item[1])
            next_step.append(str(item[2]))
            last_step.append(str(item[3]))
            print(item[1], "->", item[2])
        index = texts.index(message.text)
        table = next_step[index]
        last_table = last_step[index]
        print("Переход к финальной инструкции IT", str("t01" in next_step))
        print("Переход к финальной инструкции BIM", str("t02" in next_step))
        if "t01" in next_step or "t02" in next_step or "t1" in next_step:  # если следующая таблица пустая то вызывается
            # функция в которой выводится текст инструкции
            instruction_list = []
            for item in data:
                instruction_list.append(item[5])
            index = texts.index(message.text)
            instruction = instruction_list[index]
            table = next_step[index]
            if next_step[index] == '<-':
                data = getData(last_table)
                menu_select_step(message, data, last_table, instruction_token)
            else:
                if next_step[index] == 't1':
                    case = 1
                elif next_step[index] == 't01' or next_step[index] == 't02':
                    case = 2
                else:
                    case = 3
                data = getData(table)
                if case == 3:
                    print_instruction_step(message, instruction, data, case, table, instruction_token)
                else:
                    print_instruction_step(message, instruction, data, case, selected_table, instruction_token)

        else:  # в любом другом случае получаем данные о дальнейшем и предыдущем шаге
            # для вызова шаблонной функции генерации кнопок
            print(table)
            if table == "<-":
                data = getData(last_table)
                menu_select_step(message, data, table, instruction_token)
            else:
                data = getData(table)
                menu_select_step(message, data, table, instruction_token)
    except Exception as e:
        if message.text == "В НАЧАЛО":
            reload_bot(message)
        elif message.text == "/start":
            start(message)
        else:
            print(str(e))
            bot.reply_to(message, "Раздел")
            bot.send_message(message.chat.id, 'В данный момент не доступен', reply_markup=types.ReplyKeyboardRemove(),
                             disable_notification=True)
            reload_bot(message)

# Обычная функция генерации кнопок, ничего примечательного


def menu_select_step(message, data, table, instruction_token):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    message_list = []
    for item in data:
        if item[1] != "" and item[2] is not None and item[2] != "":
            itembtn = types.KeyboardButton(item[1])
            markup.add(itembtn)
        message_list.append(str(item[4]))
    item_btn_back = types.KeyboardButton('В НАЧАЛО')
    markup.add(item_btn_back)
    msg = bot.send_message(message.chat.id,
                           message_list[0],
                           reply_markup=markup, disable_notification=True)  # вызвать клаву
    bot.register_next_step_handler(msg, process_select_step, data, table, instruction_token)

# функция отвечает за вывод текста(далее изображений) инструкции


def print_instruction_step(message, instruction, data, case, selected_table, instruction_token):
    data = data
    print(selected_table)

    if case == 3:
        instruction_name = DecoderTableName.decode_text(selected_table)
    else:
        instruction_name = DecoderTableName.decode_text(selected_table) + f'->{message.text}'

    values = [[instruction_token, message.chat.id, instruction_name, message.text, get_date_time()[0],
               get_date_time()[1], "Без оценки"]]

    if instruction != "":

        if message.text != "Спасибо, инструкция помогла" and message.text != "Инструкция не помогла":
            sheet_data.add_interaction(values, REQUEST_BASE)

        if 'https://docs.google.com/' in instruction:
            doc = GoogleDocs(instruction)
            total_list = GoogleDocsRead(doc_body=doc.get_document_body(), inline_objects=doc.get_inline_object()
                                        ).join_total_list()
            for item in total_list:
                if item.count('googleusercontent') == 0:
                    bot.send_message(message.chat.id, item, disable_notification=True, parse_mode="HTML")
                else:
                    bot.send_photo(message.chat.id, item, disable_notification=True)
        else:
            bot.send_message(message.chat.id, instruction, disable_notification=True, parse_mode="HTML")
    base_values = sheet_data.get_sheets_values_from_base(REQUEST_BASE, start_row='2')
    base_data = sheet_data.get_dict(base_values, DICTIONARY_INSTRUCT_REQUEST)
    instruction_data = sheet_data.get_data_from_base(instruction_token, base_data, KEY_INSTRUCT_PARAM)
    if case == 1:
        print(instruction_token)
        print("Тут")
        if message.text == "Спасибо, инструкция помогла":
            effective = True
        else:
            effective = False
        sheet_data.add_rating_instruction(instruction_data, REQUEST_BASE, effective)
        reload_bot(message)
    elif case == 2:
        final_menu_select_step(message, data, instruction_token)
    elif case == 3:
        if message.text != 'Текст':
            sheet_data.add_rating_instruction(instruction_data, REQUEST_BASE, False)
            instruction_token = get_instruction_token(16)
        menu_select_step(message, data, selected_table, instruction_token)


# Последний шаг, генерируются кнопки для завершения работы (вопрос: помогло или нет?)
def final_menu_select_step(message, data, instruction_token):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    message_list = []
    for item in data:
        itembtn = types.KeyboardButton(item[1])
        message_list.append(str(item[2]))
        markup.add(itembtn)
    msg = bot.send_message(message.chat.id,
                           message_list[0],
                           reply_markup=markup, disable_notification=True)  # вызвать клаву
    bot.register_next_step_handler(msg, final_process_select_step, data, instruction_token)


# выводится тескт с дальнейшими указаниями если инструкция не помогла. (в дальнейшем здесь будет вызываться запись в БД)
def final_process_select_step(message, data, instruction_token):
    texts = []
    answers = []
    try:
        for item in data:
            texts.append(item[1])
            answers.append(item[3])
        index = texts.index(message.text)
        if message.text == "Да":
            effective = True

        else:
            effective = False
        base_values = sheet_data.get_sheets_values_from_base(REQUEST_BASE, start_row='2')
        base_data = sheet_data.get_dict(base_values, DICTIONARY_INSTRUCT_REQUEST)
        instruction_data = sheet_data.get_data_from_base(instruction_token, base_data, KEY_INSTRUCT_PARAM)
        sheet_data.add_rating_instruction(instruction_data, spreadsheet_name=REQUEST_BASE, effective=effective)
        bot.send_message(message.chat.id, answers[index], disable_notification=True)
        reload_bot(message)
    except Exception as e:
        if message.text == "В НАЧАЛО":
            reload_bot(message)
        else:
            print(str(e))
            bot.reply_to(message, 'Такого раздела пока нет')
            reload_bot(message)


if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except:
        pass

