
# coding: utf-8

# In[1]:

class time:
    "class to test overloading"
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes
        


# In[2]:

morn = time(1,45) 


# In[3]:

noon = time(1,40)


# In[4]:

total = time()


# In[5]:

total = morn + noon


# In[6]:

class time:
    "class to test overloading"
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes
    def __add__(self, data):
        temp = time()
        ta = self.hours * 60 + self.minutes
        tb = data.hours * 60 + data.minutes
        tc = ta + tb
        temp.hours = tc//60
        temp.minutes = tc%60
        return temp


# In[7]:

morn = time(1,45) 
noon = time(1,40)
total = time()


# In[8]:

total = morn + noon


# In[9]:

total.hours


# In[10]:

total.minutes


# In[11]:

eve = time(1,30)


# In[12]:

total = morn + noon + eve


# In[13]:

total.hours


# In[14]:

total.minutes


# In[ ]:



