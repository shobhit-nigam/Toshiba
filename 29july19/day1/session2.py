
# coding: utf-8

# In[1]:

vara = varb = varc = 30


# In[2]:

#multiple 


# In[3]:

vara, varb ,varc = 10, 20, 30


# In[4]:

vara = "445.67"


# In[5]:

varb = float(vara)


# In[6]:

varb


# In[7]:

vara


# In[8]:

varc = 3395601


# In[9]:

vard = str(varc)


# In[10]:

type(vard)


# In[11]:

type(varc)


# In[12]:

vard


# In[13]:

vare = 'groot'


# In[14]:

lista = list(vare)


# In[15]:

lista


# In[16]:

varx = True 
vary = False


# In[17]:

type(varx)


# In[18]:

Varx


# In[20]:

2**3


# In[23]:

1 < varb < 20


# In[24]:

#logical
# and or not 


#bitwise
# >> << & | ~ ^ 


# In[25]:

#6  0110
#4  0100


# In[26]:

6 & 4


# In[27]:

vara = 'toshiba'


# In[29]:

i = 0
while i < 7:
    print(vara[i])
    i = i+1


# In[30]:

varb = 30

if varb == 10:
    print('equal to 10')
else:
    print('not 10')


# In[33]:

varb = 30

if varb == 10:
    print('equal to 10')
elif varb == 20:
    print('equal to 20')
elif varb == 30:
    print('equal to 30')
else:
    print('not 10, not 20, not 30')


# In[35]:

varb = 30

if varb == 10:
    print('equal to 10')
elif varb == 20:
    print('equal to 20')
elif varb == 30:
    print('equal to 30')
else:
    pass
print('not 10, not 20, not 30')


# In[36]:

i = 0
while i < 7:
    print(vara[i], end =',')
    i = i+1


# In[37]:

i = 0
while i < 7:
    print(vara[i], end ='')
    i = i+1


# In[38]:

dc = ['superman', 'wonderwoman', 'flash', 'batman', 'joker', 'shazm']


# In[39]:

for hero in dc:
    print(hero)


# In[40]:

for hero in range(5):
    print(hero)


# In[42]:

for hero in range(2,5):
    print(hero)


# In[44]:

for hero in range(1,11,3):
    print(hero)


# In[46]:

for hero in dc:
    print(hero, '\t', len(hero))


# In[47]:

for hero in range(-1,-11,-4):
    print(hero)


# In[49]:

for hero in range(len(dc)):
    print(dc[hero])
    
for hero in dc:
    print(hero)


# In[50]:

#enumerate()


# In[ ]:



