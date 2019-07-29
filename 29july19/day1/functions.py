
# coding: utf-8

# In[1]:

def funca():
    print('hi')
    print('in funca')


# In[2]:

i = 0
if i < 5:
    funca()
else:
    funcb()


# In[3]:

funca = 23


# In[4]:

funca()


# In[5]:

print = 33


# In[6]:

print('hi')


# In[7]:

del print 


# In[8]:

print('hi')


# In[10]:

del funca


# In[11]:

funca()


# In[12]:

def funca():
    print('hi')
    print('in funca')


# In[13]:

def funca(varx):
    print('hi')
    print('in funca varx = ', varx)


# In[14]:

funca(23)


# In[15]:

funca()


# In[16]:

#default arguments
def funcb(varx = 30):
    print('hi')
    print('in funca varx = ', varx)


# In[17]:

funcb()


# In[18]:

funcb(20)


# In[20]:

#default arguments
def funcc(varx = 30, vary = 40):
    print('hi')
    print('in funca varx = ', varx)
    print('in funca vary = ', vary)


# In[21]:

funcc()


# In[22]:

funcc(44)


# In[23]:

#default arguments
def funcc(varx, vary = 40):
    print('hi')
    print('in funca varx = ', varx)
    print('in funca vary = ', vary)


# In[24]:

funcc(1,2)


# In[25]:

funcc(1)


# In[26]:

#default arguments
def funcd(varx = 20, vary):
    print('hi')
    print('in funca varx = ', varx)
    print('in funca vary = ', vary)


# In[27]:

#default arguments
def funcd(varx = 20, vary = 40):
    print('hi')
    print('in funca varx = ', varx)
    print('in funca vary = ', vary)


# In[28]:

funcd(vary = 100)


# In[29]:

funcd(10, varx = 100)


# In[31]:

pass


# In[32]:

for i in range(0,3):
    for j in range(0,3):
        if(i==j):
            print('tea break')
            break;
        else:
            print('no tea break')

for i in range(0,3):
    for j in range(0,3):
        if(i==j):
            print('tea break')
            continue;
        else:
            print('no tea break')
        print('coffee break')


# In[34]:

#inner function
def funcg():
    print('in fun g')
    #some code
    #some more code
    def funch():
        print('in func h')
        #some code
    #some more code
    print('last line of g')


# In[35]:

funcg()


# In[36]:

funch()


# In[37]:

#inner function
def funcg():
    print('in fun g')
    #some code
    #some more code
    def funch():
        print('in func h')
        #some code
    #some more code
    funch()
    #some more code
    #
    #
    print('last line of g')


# In[38]:

funcg()


# In[39]:

#return
def funci():
    print('in fun g')
    print('last line of g')
    return 23


# In[40]:

varx = funci()


# In[41]:

varx


# In[43]:

vara = funca(20)


# In[44]:

type(vara)


# In[45]:

#return
def funci():
    print('in fun g')
    print('last line of g')
    return 23, 45, 67


# In[46]:

vara, varb, varc = funci()


# In[47]:

vara, varb = funci()


# In[48]:

#inner function
def funcg():
    print('in fun g')
    #some code
    #some more code
    def funch():
        print('in func h')
        #some code
        return 50
    #some more code
    data = funch()
    #some more code
    #
    #
    print('last line of g')
    print('data = ', data)
    return data


# In[49]:

funcg()


# In[51]:

stringa = """
hello 
hi 
how are you 
nice dp
"""


# In[52]:

print(stringa)


# In[53]:

#return
#docstring 
def funcj():
    """
    function to show multiple return values
    """
    print('in fun g')
    print('last line of g')
    return 23, 45, 67


# In[54]:

print(funcj.__doc__)


# In[55]:

#return
#docstring 
def funck():
    "function to show multiple return values"
    print('in fun g')
    print('last line of g')
    return 23, 45, 67


# In[56]:

print(funck.__doc__)


# In[57]:

#return
#docstring 
def funck():
    print('in fun g')
    print('last line of g')
    "function to show multiple return values"
    return 23, 45, 67


# In[58]:

print(funck.__doc__)


# In[60]:

help(funcj)


# In[61]:

help(funck)


# In[62]:

#return
#docstring 
def funck():
    "function to show multiple return values"
    print('in fun g')
    print('last line of g')
    __doc__ = "updated"
    return 23, 45, 67


# In[63]:

help(funck)


# In[64]:

print(funck.__doc__)


# In[ ]:



