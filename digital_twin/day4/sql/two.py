import sqlite3

con = sqlite3.connect('chinook.db')
cur = con.cursor()
query = 'SELECT * FROM playlists'

cur.execute(query)

list_data = cur.fetchall()

print(list_data)
