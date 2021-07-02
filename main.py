import telebot
from telebot import types
import os
from data_functions import getData
from google_module import GoogleDocs, GoogleDocsRead, GoogleSheets
#import logging
import datetime
from recode_instriction_name import DecoderTableName
import secrets
import string
import logging
# не забуд прописать в терминал команду pip install pytelegrambotapi (если у тебя мак то pip3, а не pip)

logger = telebot.logger


HEROKU = os.environ.get('HEROKU')
if HEROKU == "True":
    TOKEN = os.environ.get('TOKEN')
    LINK_URL_SHEET = os.environ.get('LINK_URL_SHEET')
else:
    import config
    TOKEN = config.TOKEN
    LINK_URL_SHEET = config.LINK_URL_SHEETS

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
    print("ID обращения ", length, "16 символов:", instriction_token)
    return instriction_token


@bot.message_handler(commands=['start'])
def start(message):
    set_job_email(message)


@bot.message_handler(content_types=['text'])
def reload_bot(message):
    set_job_email(message)


def set_job_email(message):
    sheet_values = sheet_data.get_sheets_values_from_base('База пользователей', start_column='A',
                                                          start_row='2', end_column='C')
    users_parameters = {
        'user_id': "Empty value",
        'user_name': "Empty value",
        'email': "Empty value"
    }
    dict = sheet_data.get_dict(sheet_values, users_parameters)
    user_data = sheet_data.get_data_from_base(message.chat.id, dict, 'user_id')
    if user_data[0] == "Пользователя нет в базе":
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
            sheet_data.add_interaction(values, 'Демо')

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
    dictionary = {
        'instruction_token': 'none',
        'user_id': 'none',
        'path': 'none',
        'end_point': 'none',
        'date': 'none',
        'time': 'none',
        'rating': 'none'
    }
    if case == 1:
        print(instruction_token)
        print("Тут")
        if message.text == "Спасибо, инструкция помогла":
            effective = True
        else:
            effective = False
        base_values = sheet_data.get_sheets_values_from_base('Демо', start_row='2')
        base_data = sheet_data.get_dict(base_values, dictionary)
        instruction_data = sheet_data.get_data_from_base(instruction_token, base_data, 'instruction_token')
        sheet_data.add_rating_instruction(instruction_data, 'Демо', effective)
        reload_bot(message)
    elif case == 2:
        final_menu_select_step(message, data, instruction_token)
    elif case == 3:
        if message.text != 'Текст':
            base_values = sheet_data.get_sheets_values_from_base('Демо', start_row='2')
            base_data = sheet_data.get_dict(base_values, dictionary)
            instruction_data = sheet_data.get_data_from_base(instruction_token, base_data, 'instruction_token')
            sheet_data.add_rating_instruction(instruction_data, 'Демо', False)
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
        base_values = sheet_data.get_sheets_values_from_base('Демо', start_row='2')
        dictionary = {
            'instruction_token': 'none',
            'user_id': 'none',
            'path': 'none',
            'end_point': 'none',
            'date': 'none',
            'time': 'none',
            'rating': 'none'
        }
        base_data = sheet_data.get_dict(base_values, dictionary)
        instruction_data = sheet_data.get_data_from_base(instruction_token, base_data, 'instruction_token')
        sheet_data.add_rating_instruction(instruction_data, spreadsheet_name='Демо', effective=effective)
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
