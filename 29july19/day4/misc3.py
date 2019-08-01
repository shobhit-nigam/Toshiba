
# coding: utf-8

# In[1]:

lista = [7, 9, 1]


# In[2]:

for val in lista:
    print(val)


# In[7]:

def funca():
    yield 3
    yield 5
    yield 7
    yield 11


# In[8]:

for val in funca():
    print(val)


# In[9]:

obja = funca()


# In[10]:

obja


# In[11]:

obja.__next__()


# In[12]:

obja.__next__()


# In[13]:

obja.__next__()


# In[14]:

obja.__next__()


# In[15]:

obja.__next__()


# In[ ]:



