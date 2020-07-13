import sqlite3

con = sqlite3.connect('chinook.db')
cur = con.cursor()
query = 'SELECT * FROM employees'

cur.execute(query)

list_data = cur.fetchone()

print(list_data)
