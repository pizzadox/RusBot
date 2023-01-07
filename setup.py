# Подключаем SQL
import sqlite3
conn = sqlite3.connect('orders.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS constuctions(
   id INT PRIMARY KEY,
   name TEXT,
   product TEXT);
""")
cur.execute("""CREATE TABLE IF NOT EXISTS items(
   id INT PRIMARY KEY,
   name TEXT,
   construction TEXT,
   price INT);
""")

conn.commit()