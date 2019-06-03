
# coding: utf-8

# In[1]:

varx = vary = varz = 30


# In[2]:

id(varx)


# In[3]:

id(vary)


# In[4]:

id(30)


# In[5]:

varx = 34


# In[6]:

id(varx)

listc = [45, 30, 89]
# In[10]:

id(listc)


# In[11]:

id(listc[1])


# In[12]:

varx < vary == varz


# In[13]:

'a' in 'avengers'


# In[14]:

45 in listc


# In[15]:

if vary == 30:
    print("vary is 30")
    #this line
else:
    print("not 30")
    #part of else
    #part of else
print("outside")


# In[16]:

if vary == 30:
    print("vary is 30")
    #this line
elif vary < 30:
    print("less than 30")
    #part of elif
else:
    print("not 30")
    #part of else
    #part of else
print("outside")


# In[17]:

if vary == 30:
    print("vary is 30")
    #this line
elif vary < 30:
    print("less than 30")
    #part of elif
else:
    print("not 30")
    #part of else
    #part of else
print("outside")


# In[19]:

vari = 0
while vari < 5:
    print("vari=", vari, end = ' , ')
    vari = vari+1
print("outside")


# In[20]:

listc


# In[21]:

for varj in listc:
    print(varj)


# In[22]:

for varj in listc[:2]:
    print(varj)
    


# In[25]:

listd = [3, 't', 7, 8.9, 12]
for varj in range(4):
    print(varj, ',', listd[varj])

    


# In[28]:

for varj in range(1,6,2):
    print(varj)


# In[30]:

for varj in range(len(listd)):
    print("listd[varj] = ", listd[varj]) 


# In[31]:

pass 


# In[32]:

def funca():
    print("in funca")
    print("useful function")
print("outside")


# In[33]:

funca()


# In[34]:

funca


# In[35]:

type(funca)


# In[36]:

def funcb():
    print("in funca")
    print("useful function")
    return 34


# In[37]:

vard = funcb()


# In[38]:

vard 


# In[39]:

vard = funca()


# In[40]:

vard


# In[41]:

print(vard)


# In[42]:

def funcc():
    print("in funca")
    print("useful function")
    return 45, 78, 90


# In[43]:

varu, varv, varw = funcc()


# In[44]:

varv


# In[45]:

def funcd():
    print("in funca")
    print("useful function")
    return 45, 78, 90


# In[46]:

varz = funcd()


# In[47]:

varz


# In[48]:

type(varz)


# In[53]:

def funce():
    print("in e")
    print("useful")
    def funcf():
        print("in f")
        print("still in f")
        return 20
    print("lets call func f")
    funcf()
    print("back to e")
    return "hey"


# In[54]:

funce()


# In[55]:

len(funce())


# In[56]:

#vart = funce()
#vart = 'hey' 
#funce()


# In[57]:

funce.funcf()


# In[58]:

def funce():
    print("in e")
    print("useful")
    def funcf():
        print("in f")
        print("still in f")
        return 20
    print("lets call func f")
    funcf()
    print("back to e")
    return funcf()


# In[59]:

vart = funce()


# In[60]:

vart


# In[61]:

def funcg():
    "func to calculate average temp "
    print("in e")
    print("useful")
    return None


# In[62]:

print(funcg.__doc__)


# In[63]:

help(funcg)


# In[64]:

help(funce)


# In[68]:

def funch():
    print("in e")
    __doc__ = "func to calculate average temp "
    print("useful")
    return None


# In[70]:

print(funch.__doc__)


# In[71]:

varx = 5


# In[75]:

if(type(varx) is int):
    print("true")
else:
    print("false")


# In[76]:

def funcl(vara, varb):
    print("vara = ", vara)
    print("varb = ", varb)


# In[77]:

funcl(3,4)


# In[78]:

funcl(3)


# In[79]:

def funcl(vara = 34, varb = 56):
    print("vara = ", vara)
    print("varb = ", varb)


# In[81]:

funcl(8,9)


# In[82]:

funcl(8)


# In[83]:

funcl()


# In[87]:

def funcm(vara , varb = 56):
    print("vara = ", vara)
    print("varb = ", varb)


# In[85]:

funcm(7)


# In[88]:

funcm(vara = 45, varb = 33)


# In[89]:

funcl(vara = 7)


# In[90]:

funcl(varb = 7)


# In[91]:

stra = "toshiba"


# In[92]:

lista = ['koramangala', 56, 'silk']


# In[93]:

stra[0] = 'x'


# In[94]:

lista[1] = 77


# In[95]:

lista


# In[96]:

lista[0][0] = 'b'


# In[97]:

#tuple 


# In[98]:

tup_a = ('koramangala', 56, 'silk')


# In[99]:

tup_a[1] = 44


# In[100]:

tup_a = (77, 8, 9)


# In[101]:

tup_b = 5,6,


# In[102]:

type(tup_b)


# In[103]:

tup_c = 5,


# In[104]:

type(tup_c)


# In[105]:

tup_c[0]


# In[107]:

dicta = {"thor":"hammer", "hawkeye":"arrows", "shaktiman":"toofan", "krish":"mask"}


# In[108]:

print(dicta)


# In[109]:

dicta["thor"]


# In[110]:

dicta["captain"] = 'shield'


# In[111]:

dicta


# In[112]:

dicta["chotabheem"] = ['gada', 'raju', 'rani']


# In[113]:

dicta


# In[114]:

dicta["captain"] = 'hammer'


# In[115]:

dicta


# In[116]:

dicta['chotabheem'][1][2]


# In[122]:

listf = list(dicta.keys())


# In[123]:

for vari in range(len(listf)):
    print(dicta[listf[vari]])


# In[121]:

type(listf)


# In[124]:

for vari in range(len(listf)):
    print(dicta[listf[vari]])


# In[126]:

seta = {8, 9, 12, 4, 8, 3, 9}


# In[127]:

setb = {3, 9, 22, 4, 18, 3, 19}


# In[128]:

print(seta)


# In[129]:

print(setb)


# In[130]:

seta - setb 


# In[131]:

seta | setb 


# In[132]:

seta[0]


# In[ ]:



