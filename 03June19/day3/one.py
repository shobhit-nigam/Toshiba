
# coding: utf-8

# In[1]:

import sqlite3


# In[2]:

con = sqlite3.connect("cricket.db")


# In[3]:

cursor_obja = con.cursor()


# In[4]:

cursor_obja.execute("CREATE TABLE players(id integer PRIMARY KEY, name text, team text, skill text, price real, country text)")


# In[5]:

con.commit()


# In[6]:

cursor_obja.execute("""INSERT into players VALUES(30, "dhoni", "csk", "wk_bat", 678543, "ind")""")


# In[7]:

con.commit()


# In[8]:

cursor_obja.execute("""INSERT into PLAYERS (id, name, team, skill, price, country) VALUES (?,?,?,?,?,?)""", [4, "kohli", "rcb", "batsman", 783452, "ind"])


# In[9]:

con.commit()


# In[10]:

playerlista = (56, "sharmaji", "mi", "lazy_batsman", 679201, "ind")


# In[11]:

cursor_obja.execute("""INSERT into PLAYERS (id, name, team, skill, price, country) VALUES (?,?,?,?,?,?)""", playerlista)


# In[12]:

con.commit()


# In[13]:

query_string = """INSERT into PLAYERS (id, name, team, skill, price, country) VALUES (?,?,?,?,?,?)""",


# In[15]:

cursor_obja.execute('UPDATE players SET name = "rohit" where id = 56')


# In[16]:

con.commit()


# In[17]:

cursor_obja.execute('SELECT id, name FROM players')


# In[18]:

con.commit()


# In[20]:

cursor_obja.execute('SELECT id, name FROM players')
rows = cursor_obja.fetchall()
for var in rows:
    print(var)


# In[21]:

cursor_obja.execute('SELECT id, name FROM players where price > 700000')


# In[22]:

rows = cursor_obja.fetchall()


# In[23]:

for var in rows:
    print(var)


# In[24]:

print(cursor_obja.execute('SELECT * FROM players').rowcount)


# In[25]:

rows = cursor_obja.fetchall()


# In[26]:

print(len(rows))


# In[27]:

type(rows)


# In[28]:

rows


# In[29]:

cursor_obja.execute('create table if not exists worldcup(id integer primary key, name text)')


# In[32]:

con.commit()


# In[31]:

cursor_obja.execute('create table if not exists sample(id integer primary key, name text)')


# In[33]:

cursor_obja.execute('drop table if exists "sample"')


# In[34]:

con.commit()


# In[35]:

data = [(1, "sarfraz"), (2, "watson"), (3, "morgan"), (4, "gulbadeen"), (5, "russel")]
cursor_obja.executemany("insert into worldcup values (?, ?)", data)


# In[36]:

con.commit()


# In[37]:

con.close()


# In[ ]:



