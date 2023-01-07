# Импортим необходимые модули
import csv
import sqlite3

# Коннектимс к БД
connection = sqlite3.connect('../DBase/PriceList/alumark_s44.db')

# Создаем cursor
cursor = connection.cursor()

# Архитектура таблицы
create_table = """DROP TABLE aluark_s44 (
                price INTEGER PRIMARY KEY AUTOINCREMENT,
                kod_tov TEXT NOT NULL,
                art TEXT NOT NULL,
                name TEXT NOT NULL);
                """

# Создаем таблицу в БД
cursor.execute(create_table)

# Открываем CSV
file = open('../DBase/input/alumark_s44.csv')

# Читаем CSV
contents = csv.reader(file)

# SQL запрос

insert_records = "INSERT INTO aluark_s44 (price, kod_tov, art, name) VALUES(?, ?, ?, ?)"

# Импортируемданные в таблицу базы
cursor.executemany(insert_records, contents)

# SQL-запрос для извлечения всех данных из
# таблицы aluark_s44, чтобы убедиться, что
# данные csv-файла были успешно
# вставлены в таблицу
select_all = "SELECT * FROM aluark_s44"
rows = cursor.execute(select_all).fetchall()

# Вывод в консоль
for r in rows:
    print(r)

# Коммитим изминения
connection.commit()

# Закрываем соединение
connection.close()