
# coding: utf-8

# In[1]:

rava = 'rava'
choco = 'choco'


# In[3]:

def funca(x):
    print("making", x, "laddos")


# In[4]:

funca(rava)


# In[5]:

def funcb(x):
    print("making", x, "modaks")


# In[6]:

funca(rava)
funcb(choco)


# In[7]:

def make(gen, x):
    gen(x)


# In[8]:

make(funa, rava)


# In[10]:

make(funcb, rava)


# In[11]:

def funca():
    print('plain Ganesha')

def funcb(gen):
    def funcc():
        gen()
        print('decorated Ganesha')
    return funcc


# In[13]:

funcx = funcb(funca)


# In[14]:

funca()


# In[15]:

funcx()


# In[16]:

#funcx is the decorated function


# In[17]:

def funca():
    print('plain Ganesha')

def funcb(gen):
    def funcc():
        gen()
        print('decorated Ganesha')
    return funcc

funca()
print('-----------')
funca = funcb(funca)
funca()


# In[18]:

def funcb(gen):
    def funcc():
        gen()
        print('decorated Ganesha')
    return funcc

def funca():
    print('plain Ganesha')
funca = funcb(funca)
funca()


# In[19]:

def funcb(gen):
    def funcc():
        gen()
        print('decorated Ganesha')
    return funcc

@funcb
def funca():
    print('plain Ganesha')
#funca = funcb(funca)


# In[20]:

funca()


# In[23]:

def hashtag(func):
    def inner(*args):
        print("#"*20)
        func(*args)
        print("#"*20)
    return inner

@hashtag
def display(data):
    print(data)
#display = hashtag(display)


# In[25]:

display('hello')


# In[26]:

def tilde(func):
    def inner(*args):
        print("~"*20)
        func(*args)
        print("~"*20)
    return inner

def hashtag(func):
    def inner(*args):
        print("#"*20)
        func(*args)
        print("#"*20)
    return inner

@tilde
@hashtag
def display(data):
    print(data)
#display = hashtag(display)


# In[28]:

display('hi')


# In[ ]:

def tilde(func):
    def inner(*args):
        print("~"*20)
        func(*args)
        print("~"*20)
    return inner

def hashtag(func):
    def inner(*args):
        print("#"*20)
        func(*args)
        print("#"*20)
    return inner

@tilde
@hashtag
def display(data):
    print(data)

@hashtag
def display2(data):
    print(data)

