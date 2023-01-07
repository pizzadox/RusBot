
import csv
import sqlite3


connection = sqlite3.connect('../DBase/PriceList/alumark_s44.db')

cursor = connection.cursor()

create_table = """CREATE TABLE IF NOT EXISTS alumark_s44 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                price TEXT NOT NULL,
                kod_tov TEXT NOT NULL,
                art TEXT NOT NULL,
                name TEXT NOT NULL);
                """

cursor.execute(create_table)

file = open('../DBase/input/alumark_s44.csv')

contents = csv.reader(file)

insert_records = "INSERT INTO alumark_s44 (price, kod_tov, art, name) VALUES(?, ?, ?, ?)"

cursor.executemany(insert_records, contents)

select_all = "SELECT * FROM alumark_s44"
rows = cursor.execute(select_all).fetchall()

for r in rows:
    print(r)

connection.commit()

connection.close()