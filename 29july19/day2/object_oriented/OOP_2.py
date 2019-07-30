
# coding: utf-8

# In[1]:

class spartans:
    "sample to understand classes"
    gear = 'swords'
    def fight(self):
        print('spartans fight well')
        print(self.gear)


# In[2]:

help(spartans)


# In[3]:

print(spartans.__doc__)


# In[5]:

class spartans:
    "sample to understand classes"
    def __init__(self):
        print("inside init of spartans")
    gear = 'swords'
    def fight(self):
        print('spartans fight well')
        print(self.gear)


# In[6]:

obja = spartans()


# In[10]:

class spartans:
    "sample to understand classes"
    def __init__(self, x=0, y=0):
        print("inside init of spartans")
    gear = 'swords'
    def fight(self):
        print('spartans fight well')
        print(self.gear)


# In[11]:

objb = spartans(6, 90)


# In[12]:

obja = spartans()


# In[13]:

class spartans:
    "sample to understand classes"
    gear = 'swords'
    varx = 0
    vary = 10
    def __init__(self, x=0, y=0):
        print("inside init of spartans")
        self.varx = x
        self.vary = y
    def fight(self):
        print('spartans fight well')
        print(self.gear)


# In[14]:

obja = spartans()
objb = spartans(6, 90)


# In[15]:

obja.__init__()


# In[23]:

class ironman:
    gear = 'suit'
    def fly(self):
        print('iron man flies')
    def fight(self):
        print('fights with iron shield')


# In[24]:

class hulkbuster(ironman):
    def destroy(self):
        print("destroys cities")


# In[25]:

obji = ironman()


# In[26]:

objh = hulkbuster()


# In[27]:

objh.destroy()


# In[32]:

class ironman:
    def __init__(self):
        print("inside init of spartans")
    gear = 'suit'
    def fly(self):
        print('iron man flies')
    def fight(self):
        print('fights with iron shield')

class hulkbuster(ironman):
    def __init__(self):
        print('init of hulkbuster')
    def destroy(self):
        print("destroys cities")        


# In[33]:

obji = ironman()
objh = hulkbuster()


# In[45]:

class ironman:
    def __init__(self):
        print("inside init of spartans")
    gear = 'suit'
    def fly(self):
        print('iron man flies')
    def fight(self):
        print('fights with iron shield')
    def funcx(self):
        print('x of ironman')

class stanlee:
    def __init__(self):
        print("inside init of stanlees")
    def creativity(self):
        print("stanlee's creativity")
    def funcx(self):
        print('x of stanlee')

class hulkbuster(stanlee,ironman):
    def destroy(self):
        print("destroys cities")  



# In[46]:

objh = hulkbuster()


# In[47]:

objh.funcx()


# In[ ]:



