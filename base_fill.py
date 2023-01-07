import sqlite3
conn = sqlite3.connect('orders.db')
cur = conn.cursor()
cur.execute("INSERT INTO constuctions VALUES(1, Krauss, KRDW45);")
conn.commit()