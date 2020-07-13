import sqlite3

con = sqlite3.connect('chinook.db')
cur = con.cursor()
query = 'SELECT * FROM employees '

cur.execute(query)

list_data = cur.fetchall()

with open("employee_a.txt", "w") as fa:
    for line in list_data:
        fa.write(line[2])
        fa.write(" ")
        fa.write(line[1])
        fa.write(" ")
        fa.write(line[-1])
        fa.write("\n")
    
#print(list_data)

