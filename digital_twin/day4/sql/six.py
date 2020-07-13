import sqlite3

con = sqlite3.connect('sports.db')
cur = con.cursor()
query = '''INSERT into players VALUES (10, "shafali", "cricket", 234600)'''

cur.execute(query)
con.commit()

con.close()
