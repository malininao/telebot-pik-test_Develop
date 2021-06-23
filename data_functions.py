import sqlite3

with sqlite3.connect('data.db',  check_same_thread=False) as db:
    cursor = db.cursor()

def getData(table):
    data = []
    dataList = cursor.execute(f"""SELECT * FROM {table}""")
    for item in dataList:
        data.append(item)
    return data


if __name__ == "__main__":
    pass





