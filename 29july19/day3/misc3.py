
# coding: utf-8

# In[1]:

varg = 20
def funca():
    print(varg)
    varg = 30
    print(varg)


# In[2]:

funca()


# In[5]:

varg = 20
def funca():
    print(varg)
    varg = 30
#    print(varg)


# In[6]:

funca()


# In[7]:

lista = []


# In[8]:

for var in 'toshiba':
    lista.append(var)


# In[9]:

lista


# In[10]:

#list comprehensions


# In[11]:

listb = [var for var in 'toshiba']


# In[12]:

listb


# In[13]:

listn = [x for x in range(16) if x%2 == 0]


# In[14]:

listn


# In[15]:

get_ipython().magic('ls')


# In[16]:

get_ipython().magic('lsmagic')


# In[18]:

get_ipython().run_cell_magic('ruby', '', 'print "hello ruby"')


# In[19]:

get_ipython().magic('pinfo %run')


# In[1]:

get_ipython().magic('save misc4 7-10')


# In[2]:

get_ipython().magic('pinfo %save')


# In[ ]:



