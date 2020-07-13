import sqlite3

con = sqlite3.connect('sports.db')
cur = con.cursor()
#query = '''INSERT into players VALUES (10, "shafali", "cricket", 234600)'''
query = '''INSERT into players (id, name, skill, price) VALUES (?, ?, ?, ?)'''
listx = [20, 'dutee chand', 'athlete', 234000]

cur.execute(query, listx)
con.commit()



with open("players.txt", "r") as fa:
    stra = fa.read()

data = []
lista = stra.splitlines()
for line in lista:
    tempx = line.split()
    tempy = []
    tempy.append(int(tempx[0]))
    tempy.append(tempx[1]+ " " + tempx[2])
    tempy.append(tempx[3])
    tempy.append(int(tempx[4]))
    data.append(tempy)


con.close()
