import sqlite3
import os
from psycopg2 import connect
from datetime import datetime
from google_module import GoogleSheets
import asyncio

def get_date_time():
    offset = datetime.timedelta(hours=3)
    dt = datetime.datetime.now(tz=datetime.timezone(offset, 'МСК'))
    date = f'{dt.date().day}.{dt.date().month}.{dt.date().year}'
    time = f'{dt.time().hour}:{dt.time().minute}:{dt.time().second}'
    return date, time

if os.environ.get('HEROKU') == "True":
    DATABASE_URL = os.environ['DATABASE_URL']
    sslmode = 'require'
    params = {'dsn': DATABASE_URL, 'sslmode': 'require'}
else:
    import config
    DATABASE = config.DATABASE
    DATABASE_USER = config.DATABASE_USER
    DATABASE_PASSWORD = config.DATABASE_PASSWORD
    DATABASE_HOST = config.DATABASE_HOST
    DATABASE_PORT = config.DATABASE_PORT
    params = {'database': config.DATABASE, 'user': config.DATABASE_USER, 'password': config.DATABASE_PASSWORD,
              'host': config.DATABASE_HOST, 'port': config.DATABASE_PORT}


with sqlite3.connect('data.db',  check_same_thread=False) as db:
    cursor = db.cursor()


class DataBaseFunctions:

    @staticmethod
    def insert_data_in_base_by_token(data, table_name):
        with connect(**params) as conn:
            cur = conn.cursor()
            for item in data:
                cur.execute(f'''INSERT INTO {table_name} VALUES {item[1]}''')
            print('data was written')

    @staticmethod
    def select_data(table_name: str):
        with connect(**params) as conn:
            cur = conn.cursor()
            cur.execute(f'''SELECT * FROM {table_name}''')
            data = cur.fetchall()
            print(data)
            return data

    @staticmethod
    def recreate_table(table_name: str):
        with connect(**params) as conn:
            print('connection establish')
            cur = conn.cursor()
            cur.execute('''DROP TABLE %s''' % table_name)
            print('table deleted')
            cur.execute('''CREATE TABLE requests 
                         (REQUEST_TOKEN TEXT PRIMARY KEY NOT NULL UNIQUE,
                         USER_ID TEXT NOT NULL,
                         PATH TEXT NOT NULL,
                         END_POINT TEXT NOT NULL,
                         DATE TEXT NOT NULL,
                         TIME TEXT NOT NULL,
                         RATING TEXT NOT NULL);''')
            print('table created')

    @staticmethod
    def create_table():
        with connect(**params) as conn:
            print('connection establish')
            cur = conn.cursor()
            cur.execute('''CREATE TABLE requests 
                     (REQUEST_TOKEN TEXT PRIMARY KEY NOT NULL UNIQUE,
                     USER_ID TEXT NOT NULL,
                     PATH TEXT NOT NULL,
                     END_POINT TEXT NOT NULL,
                     DATE TEXT NOT NULL,
                     TIME TEXT NOT NULL,
                     RATING TEXT NOT NULL);''')
            print('table created')

    @staticmethod
    def drop_table(table_name):
        with connect(**params) as conn:
            print('connection establish')
            cur = conn.cursor()
            cur.execute('''DROP TABLE %s''' % table_name)
            print('table deleted')


class ImportFunction:

    @staticmethod
    def import_in_google_sheet(SHEET_URL: str, spreadsheet_name: str, table_name: str):
        data = DataBaseFunctions.select_data(table_name)
        GoogleSheets(SHEET_URL).add_interaction(spreadsheet_name=spreadsheet_name, values=data)
        DataBaseFunctions.recreate_table(table_name)


def get_data(table):
    data = []
    data_list = cursor.execute(f"""SELECT * FROM {table}""")
    for item in data_list:
        data.append(item)
    return data


def update_rating(instriction_token, rating):
    with connect(**params) as conn:
        cur = conn.cursor()
        cur.execute(f'''UPDATE requests 
                        SET rating = %s 
                        WHERE request_token = %s''' % (rating, instriction_token))
        print(f'request data with token {instriction_token} was updated')


class DataCash:

    def __init__(self):
        self.values = []

    def add_value(self, value):
        self.values.append(value)
        return self.values

    def write_values(self, table_name, max_count_element):
        if len(self.values) >= max_count_element:
            DataBaseFunctions.insert_data_in_base_by_token(self.values, table_name)
            self.values = []
        else:
            pass




if __name__ == "__main__":
    ImportFunction.import_in_google_sheet(config.LINK_URL_SHEETS, 'Демо', 'requests')










