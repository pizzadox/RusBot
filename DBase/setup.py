# Подключаем SQL
import sqlite3
conn = sqlite3.connect('../orders.db')
cur = conn.cursor()

# Создаем таблицы
    # Таблица в которой лежат ИД/Производитель/Серия
cur.execute("""CREATE TABLE IF NOT EXISTS constuctions(
   id INT PRIMARY KEY,
   name TEXT,
   product TEXT);
""")
    # Таблиа в которой лежат ИД/Название/Материал/Стоимость
cur.execute("""CREATE TABLE IF NOT EXISTS items(
   id INT PRIMARY KEY,
   name TEXT,
   construction TEXT,
   price INT);
""")

conn.commit()