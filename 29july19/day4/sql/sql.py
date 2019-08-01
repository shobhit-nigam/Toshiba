
# coding: utf-8

# In[1]:

import sqlite3


# In[2]:

cona = sqlite3.connect('cricket.db')


# In[3]:

curs = cona.cursor()


# In[4]:

type(curs)


# In[5]:

curs.execute("CREATE TABLE players(id integer PRIMARY KEY, name text, team text, skill text, price real, country text)")


# In[6]:

#cona.commit()


# In[7]:

curs.execute("INSERT into players VALUES(10, 'sachin', 'mi', 'batsmen', 600000, 'india')")


# In[8]:

cona.commit()


# In[9]:

curs.execute("INSERT into players (id, name, team, skill, price, country) VALUES(?,?,?,?,?,?)" , 
[18, 'virat', 'rcb', 'batsmen', 500000, 'india'])


# In[10]:

cona.commit()


# In[11]:

query = "INSERT into players (id, name, team, skill, price, country) VALUES(?,?,?,?,?,?)"
lista = [20, 'lara', 'trinidad', 'batsmen', 300000, 'wi']


# In[12]:

curs.execute(query, lista)


# In[13]:

cona.commit()


# In[14]:

def funca(q, v):
    curs.execute(q, v)


# In[15]:

curs.execute("UPDATE players SET name = 'god' where id = 10")
cona.commit()


# In[16]:

curs.execute("SELECT * FROM players")


# In[17]:

data = curs.fetchall()


# In[18]:

data


# In[24]:

curs.execute("SELECT * FROM players WHERE country = 'india'")


# In[25]:

data = curs.fetchall()


# In[26]:

data


# In[27]:

cona.close()


# In[28]:

import pandas as pd
import sqlite3

conb = sqlite3.connect('cricket.db')
query = "SELECT * FROM players WHERE country = 'india'"

dfa = pd.read_sql_query(query, conb)


# In[29]:

dfa


# In[ ]:



