import sqlite3
from sqlite3.dbapi2 import Cursor

conn = sqlite3.connect('db_bsp.db')
#conn.execute('CREATE TABLE users (name TEXT, addr TEXT)')
name = ["dig1", "dig2"]
addr = ["test", "test2"]

list_ready = list(zip(name, addr))
#print(*list_ready)
curs = conn.cursor()
curs.executemany("insert into users (name, addr) VALUES (?,?)", list_ready)
conn.commit()

curs.execute("select * from users")
print(curs.fetchall())

conn.close()