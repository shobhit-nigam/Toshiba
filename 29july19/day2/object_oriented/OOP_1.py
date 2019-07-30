
# coding: utf-8

# In[1]:

class spartans:
    gear = 'swords'
    defend_gear = 'shields'
    def fight():
        print('spartans fight well')
    def shout():
        print('spartaaaaa')


# In[2]:

obja = spartans()


# In[3]:

obja.gear


# In[4]:

spartans.fight()


# In[5]:

obja.fight()


# In[6]:

class spartans:
    gear = 'swords'
    defend_gear = 'shields'
    def fight(ttt):
        print('spartans fight well')
    def shout(yyy):
        print('spartaaaaa')


# In[8]:

obja = spartans()
obja.fight()
#spartans.fight(obja)


# In[9]:

class spartans:
    gear = 'swords'
    defend_gear = 'shields'
    def fight(self):
        print('spartans fight well')
    def shout(self):
        print('spartaaaaa')


# In[11]:

spartans.fight('randome value')
#spartans.fight()


# In[12]:

class spartans:
    gear = 'swords'
    defend_gear = 'shields'
    def fight(self, vara, varb):
        print('spartans fight well')
    def shout(self):
        print('spartaaaaa')


# In[13]:

objb = spartans()


# In[14]:

objb.fight(6, 7)


# In[21]:

class spartans:
    gear = 'swords'
    defend_gear = 'shields'
    def fight(self):
        print('spartans fight well')
        if self.gear == 'spears':
            print('objb called the function')
        else:
            print(self.gear)
    def shout(self):
        print('spartaaaaa')


# In[22]:

objb = spartans()


# In[18]:

objb.fight()
#spartans.fight(objb)
self = objb


# In[19]:

objb.gear = 'spears'


# In[23]:

objc = spartans()


# In[24]:

objb = spartans()
objc = spartans()


# In[25]:

objb.gear = 'spears'


# In[26]:

objb.fight()


# In[27]:

objc.fight()


# In[28]:

obja = spartans()
spartans.fight(obja)


# In[31]:

class spartans:
    gear = 'swords'
    defend_gear = 'shields'
    def fight(self):
        print('spartans fight well')
        print(self.gear)
        print(self.defend_gear)
        self.x = 30
    def shout(self):
        print('spartaaaaa')


# In[32]:

objb = spartans()
objc = spartans()
obja = spartans()


# In[33]:

obja.fight()


# In[34]:

obja.x


# In[35]:

objb.x


# In[36]:

obja.y = 45


# In[37]:

spartans.x


# In[40]:

class spartans:
    gear = 'swords'
    __wear = 'leather'
    __care__ = 'sparta'
    def fight(self):
        print('spartans fight well')
        print(self.gear)
        print(self.__wear)
        print(self.__care__)


# In[41]:

obja = spartans()


# In[42]:

obja.fight()


# In[43]:

obja.gear


# In[44]:

obja.__wear


# In[45]:

obja.__care__


# In[46]:

spartans.__wear


# In[47]:

obja.__wear = 'new leather'


# In[ ]:



