cur.execute("""CREATE TABLE IF NOT EXISTS constuctions(
   id INT PRIMARY KEY,
   name TEXT,
   product TEXT;
""")
conn.commit()