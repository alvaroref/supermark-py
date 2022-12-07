import sqlite3 as sql



con = sql.connect('supermark.db')
cur = con.cursor()
nombre = "naranja"
cur.execute(f"select * from productos where nombre = '{nombre}'")
prod = cur.fetchone()
print(prod[3])

cur.execute(f"")
con.close()
