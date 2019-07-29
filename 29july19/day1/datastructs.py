
# coding: utf-8

# In[1]:

lista = [9, 10, 20]


# In[2]:

lista[1] = 33


# In[3]:

lista


# In[4]:

listb = (9, 10, 20)


# In[5]:

listb[1] = 33


# In[6]:

#tuple


# In[7]:

listb = list(listb)


# In[8]:

listb


# In[9]:

dicty= {'thor':'hammer', 'avengers':['ironman', 'antman']}


# In[10]:

dicty['thor']


# In[11]:

dicty['avengers']


# In[12]:

dicty['avengers'][0]


# In[14]:

varx = 20
vary = 33


# In[15]:

dictx = {varx:'hi', vary:dicty}


# In[16]:

dicty


# In[18]:

dictx[vary]['avengers'][1][1]


# In[20]:

print(dictx.keys())


# In[21]:

listy = list(dicty.keys()) 


# In[22]:

listy


# In[23]:

#unordered


# In[24]:

seta = {12, 14, 8, 'hi', 23, 12, 8, 33}


# In[25]:

seta


# In[26]:

#listc = (3)
(3 + 10) * 2


# In[27]:

listc = (3)


# In[28]:

type(listc)


# In[29]:

listc = (3,)


# In[30]:

type(listc)


# In[31]:

listd = 5,


# In[32]:

#return
def funci():
    print('in fun g')
    print('last line of g')
    return 23, 45, 67


# In[33]:

vara = funci()


# In[34]:

type(vara)


# In[35]:

seta = {12, 14, 8, 'hi', 23, 12, 8, 33}
setb = {12, 'hello', 23, 11, 8, 34}


# In[39]:

seta | setb


# In[ ]:



