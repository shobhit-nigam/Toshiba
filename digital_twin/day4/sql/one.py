import sqlite3

con = sqlite3.connect('chinook.db')
cur = con.cursor()
query = 'SELECT name from sqlite_master where type="table"'

cur.execute(query)

list_tables = cur.fetchall()

print(list_tables)
