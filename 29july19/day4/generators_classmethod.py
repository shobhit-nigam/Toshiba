
# coding: utf-8

# In[2]:

class sample:
    varx = 30
    vary = 40
    def __init__(self, x, y):
        self.varx = x
        self.vary = y
    
    def funca(self):
        self.varx = 5
    
    def funcb(self):
        self.vary = 15
    
    def __str__(self):
        stra = 'varx = {} vary = {}'.format(self.varx, self.vary)
        return stra


# In[5]:

obja = sample(30, 40)
objb = sample(100, 200)


# In[4]:

obja.varx


# In[6]:

obja.funca()


# In[7]:

obja.varx


# In[8]:

objb.varx


# In[9]:

objc = sample(70, 80)


# In[10]:

print(obja)


# In[11]:

class sample:
    varx = 30
    vary = 40
    def __init__(self, x, y):
        self.varx = x
        self.vary = y
    
    
    def funca(self):
        self.varx = 5
    
    def funcb(self):
        self.vary = 15
    
    def __str__(self):
        stra = 'varx = {} vary = {}'.format(self.varx, self.vary)
        return stra


# In[12]:

obja = sample(30, 40)
objb = sample(100, 200)


# In[13]:

print(obja)


# In[14]:

obja


# In[15]:

class sample:
    varx = 30
    vary = 40
    def __init__(self, x, y):
        self.varx = x
        self.vary = y
    
    @classmethod
    def funca(class_name):
        class_name.varx = 5
        #sample.varx
    
    def funcb(self):
        self.vary = 15
    
    def __str__(self):
        stra = 'varx = {} vary = {}'.format(self.varx, self.vary)
        return stra


# In[16]:

obja = sample(30, 40)
objb = sample(100, 200)


# In[17]:

obja.funca()


# In[18]:

obja.varx


# In[19]:

sample.varx


# In[26]:

class sample:
    varx = 30
    vary = 40
    def __init__(self, x, y):
        self.varx = x
        self.vary = y
    
    @classmethod
    def funca(class_name):
        class_name.varx = 5
        #sample.varx
    
    @staticmethod
    def funcb():
        print('hi')
        global varx
        varx = 45
    
    def __str__(self):
        stra = 'varx = {} vary = {}'.format(self.varx, self.vary)
        return stra


# In[27]:

obja = sample(30, 40)
objb = sample(100, 200)


# In[28]:

obja.funcb()


# In[30]:

objb.funcb()


# In[31]:

class sample:
    varx = 30
    vary = 40
    def __init__(self, x, y):
        self.varx = x
        self.vary = y
    
    @classmethod
    def funca(class_name):
        class_name.varx = 5
        #sample.varx
    
    @staticmethod
    def funcb():
        print('hi')
        global varx
        varx = 45
    
    def __str__(self):
        stra = 'varx = {} vary = {}'.format(self.varx, self.vary)
        return stra


# In[32]:

obja.funcb()


# In[33]:

obja.varx


# In[34]:

sample.varx


# In[ ]:



