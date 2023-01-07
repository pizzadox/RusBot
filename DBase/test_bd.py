import sqlite3 as db
conn = db.connect('../DBase/PriceList/alumark_s44.db')
conn.row_factory = lambda cursor, row: row[0]
c = conn.cursor()
ids = c.execute('SELECT name FROM aluark_s44').fetchall()