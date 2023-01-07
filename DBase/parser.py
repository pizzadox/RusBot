# �������� ����������� ������
import csv
import sqlite3

# ���������� � ��
connection = sqlite3.connect('../DBase/PriceList/alumark_s44.db')

# ������� cursor
cursor = connection.cursor()

# ����������� �������
create_table = """DROP TABLE aluark_s44 (
                price INTEGER PRIMARY KEY AUTOINCREMENT,
                kod_tov TEXT NOT NULL,
                art TEXT NOT NULL,
                name TEXT NOT NULL);
                """

# ������� ������� � ��
cursor.execute(create_table)

# ��������� CSV
file = open('../DBase/input/alumark_s44.csv')

# ������ CSV
contents = csv.reader(file)

# SQL ������

insert_records = "INSERT INTO aluark_s44 (price, kod_tov, art, name) VALUES(?, ?, ?, ?)"

# ����������������� � ������� ����
cursor.executemany(insert_records, contents)

# SQL-������ ��� ���������� ���� ������ ��
# ������� aluark_s44, ����� ���������, ���
# ������ csv-����� ���� �������
# ��������� � �������
select_all = "SELECT * FROM aluark_s44"
rows = cursor.execute(select_all).fetchall()

# ����� � �������
for r in rows:
    print(r)

# �������� ���������
connection.commit()

# ��������� ����������
connection.close()