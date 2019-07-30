
# coding: utf-8

# In[2]:

varx = input()
print(varx)


# In[3]:

vary = input()


# In[4]:

print(vary)


# In[5]:

type(varx)


# In[6]:

type(vary)


# In[7]:

vary


# In[8]:

vary = int(input())


# In[9]:

type(vary)


# In[10]:

varz = eval(input())


# In[12]:

type(varz)


# In[13]:

varz = eval(input())


# In[14]:

type(varz)


# In[15]:

varz = eval(input())


# In[16]:

type(varz)


# In[17]:

varz = eval(input())


# In[18]:

type(varz)


# In[20]:

varz = eval(input())


# In[21]:

varz


# In[22]:

#funcyional composition
varz = eval(input("print sting with quotes: "))


# In[23]:

print('varx = ', varx, "vary = ", vary)


# In[29]:

"vary = ", vary


# In[30]:

print('a number--> {} and another string--> {}'.format(23, "str"))


# In[31]:

print('a number--> {} and another string--> {}'.format(varx, vary))


# In[32]:

dicta = {2:'hi', 5:'hello', 19:20}


# In[33]:

for k, v in dicta.items():
    print(k ,'\t', v)


# In[34]:

for k, v in dicta.items():
    print("%s = %s" %(k,v))


# In[35]:

lista = ['aa', 'bb', 'cc']
listb = [23, 56, 77]


# In[36]:

dictb = dict(zip(lista, listb))


# In[37]:

type(dictb)


# In[38]:

for k, v in dictb.items():
    print(k ,'\t', v)


# In[41]:

lista = ['aa', 'bb', 'cc']
listb = [22, 55, 67, 90]


# In[42]:

dictb = dict(zip(lista, listb))


# In[43]:

for k, v in dictb.items():
    print(k ,'\t', v)


# In[44]:

type(dict)


# In[47]:

pass


# In[48]:

pass


# In[49]:

def funca():
    print('in a')


# In[50]:

f = funca()


# In[51]:

f = funca


# In[52]:

f()


# In[53]:

def funcb(varx, vary):
    print('in b')
    print(varx)
    print(vary)


# In[54]:

def funcb(*xxx):
    print('in b')
    for val in xxx:
        print("xxx = ", val)


# In[55]:

funcb(56, 78)


# In[56]:

def funcb(*args):
    print('in b')
    for val in args:
        print("val = ", val)


# In[57]:

funcb(5,7,"hi", [7,8,9])


# In[61]:

def funcc(arg1, *args):
    for val in args:
        print("val = ", val)


# In[62]:

funcc(6, 8, 9)


# In[63]:

def funcc(*args, arg1):
    for val in args:
        print("val = ", val)


# In[64]:

funcc(6, 8, 9)


# In[65]:

def funcd(**kwargs):
    for k, v in kwargs.items():
        print(k ,'\t', v)


# In[66]:

funcd(29 = 'mon', 30 = 'tue', 31 = 'wed')


# In[69]:

funcd(varx = 'mon', vary = 'tue', varz = 30)


# In[70]:

def funcd(**kwargs):
    for k, v in kwargs.items():
        print(k ,'\t', v)


# In[71]:

funcd(varx = 'mon', vary = 'tue', varz = 30)


# In[72]:

vary


# In[75]:

varz = 32
funcd(varx = 'mon', vary = 'tue', varz = varz)


# In[77]:

varz = 32
funcd(varx = 'mon', vary = 'tue', varz = varz)


# In[78]:

#global, local, nonlocal


# In[79]:

#high order functions


# In[80]:

def eat(funcx):
    print('going to eat')
    funcx()


# In[81]:

def seven():
    print('eating upstairs')


# In[83]:

def home():
    print('having home food')


# In[84]:

def mustard():
    print('having mustard biryani')


# In[85]:

eat(seven)


# In[86]:

eat(mustard)


# In[87]:

def eat(funcx, time):
    print('going to eat for ', time, 'hours')
    funcx()


# In[88]:

eat(home, 0.5)


# In[89]:

def mustard(biryani= 'veg'):
    print('having' , biryani, 'biryani')


# In[90]:

#will throw an error
eat(mustard, 1)


# In[ ]:



