
# coding: utf-8

# In[1]:

varc = input()


# In[2]:

print(varc)


# In[3]:

vard = input()


# In[4]:

type(varc)


# In[5]:

type(vard)


# In[6]:

vard = int(vard)


# In[7]:

type(vard)


# In[8]:

vard = int(input())


# In[9]:

type(vard)


# In[11]:

vare = int(input("plz enter a value: ")) 


# In[12]:

vare = int(56.78)


# In[13]:

vare


# In[14]:

varf = eval(input("plz enter a value: "))


# In[15]:

type(varf)


# In[16]:

varg = eval(input("plz enter a value: "))


# In[17]:

varg


# In[19]:

varh = eval(input("plz enter a value: "))


# In[20]:

varh = eval(input("plz enter a value: "))


# In[21]:

varh = eval(input("plz enter a value: "))


# In[22]:

x, y = input()


# In[23]:

type(x)


# In[24]:

type(y)


# In[26]:

pass


# In[27]:

10/0


# In[28]:

print(keshab)


# In[31]:

lista = [6]
avg = 1
avg = sum(lista)/len(lista)


# In[32]:

lista = []
avg = 1
avg = sum(lista)/1


# In[33]:

try:
    lista = []
    avg = 1
    avg = sum(list_a)/len(list_a)
    print(avg)
except NameError:
    print("you got the name wrong")
print("outside try")


# In[35]:

try:
    print("starting try block")
    lista = []
    avg = 1
    avg = sum(lista)/len(lista)
    print(avg)
except NameError:
    print("you got the name wrong")
except ZeroDivisionError:
    print("you cant divide by zero")
print("outside try")


# In[36]:

try:
    print("starting try block")
    lista = [6,7]
    avg = 1
    avg = sum(lista)/len(lista)
    print(avg)
except NameError:
    print("you got the name wrong")
except ZeroDivisionError:
    print("you cant divide by zero")
print("outside try")


# In[38]:

try:
    print("starting try block")
    lista = [6,7]
    avg = 1
    avg = sum(lista)/len(lista)
    print(avg)
    print(lista[2])
except NameError:
    print("you got the name wrong")
except ZeroDivisionError:
    print("you cant divide by zero")
except:
    
print("outside try")


# In[39]:

try:
    print("starting try block")
    lista = [6,7]
    avg = 1
    avg = sum(lista)/len(lista)
    print(avg)
    print(lista[2])
except NameError:
    print("you got the name wrong")
except ZeroDivisionError:
    print("you cant divide by zero")
except:
    print("some error")
print("outside try")


# In[40]:

try:
    print("starting try block")
    lista = [6,7]
    avg = 1
    avg = sum(lista)/len(lista)
    print(avg)
    print(lista[2])
except:
    print("some error")
except NameError:
    print("you got the name wrong")
except ZeroDivisionError:
    print("you cant divide by zero")
    
print("outside try")


# In[42]:

try:
    print("starting try block")
    lista = [6,7]
    avg = 1
    avg = sum(lista)/len(lista)
    print(avg)
    print(lista[2])
except NameError:
    print("you got the name wrong")
except ZeroDivisionError:
    print("you cant divide by zero")
except:
    print("some error")
    
print("outside try")


# In[43]:

def funca(a, b):
    varx = a/b
    print(varx)


# In[44]:

funca(5,6)


# In[45]:

funca(5,0)


# In[51]:

def funca(a, b):
    try:
        varx = a/b
    except :
        print("some error")
    else :
        print(varx)


# In[49]:

funca(5, 10)


# In[50]:

funca(5, 0)


# In[53]:

lista = [3, 7, 10, 5]
try :
    n = int(input("enter a num: "))
    if(n<=0):
        raise ValueError("not a positive number")
    else:
        print(lista[n])
except ValueError as data:
    print("type of ", type(data))
    print(data)


# In[54]:

lista = [3, 7, 10, 5]
try :
    n = int(input("enter a num: "))
    if(n<=0):
        raise ValueError("not a positive number")
    else:
        print(lista[n])
except ValueError as data:
    print("type of ", type(data))
    print(data)


# In[55]:

try:
    try:
        #some exception raised
    except ValueError: 
        #eee
        #raise 
    except NameError:
        #hhh
except:
    #rrrr


# In[56]:

try:
    funca(2,0)
except:
    pass


# In[59]:

#Exception class
class AppError(Exception):
    """base class for all exceptions"""
    pass

class SmallValue(AppError):
    """raised when val is too small"""
    pass

class LargeValue(AppError):
    """raised when val is too large"""
    pass


# In[60]:

val = 20
while True:
    try:
        num = int(input("enter a num"))
        if num < val:
            raise SmallValue
        elif num > val:
            raise LargeValue
        break
    except SmallValue:
        print(SmallValue.__doc__)
    except LargeValue:
        print(LargeValue.__doc__)

print("wow, guessed it correctly")


# In[61]:

def funcb(*argv):
    for var in argv:
        print(var)


# In[62]:

funcb("i am", "hungry")


# In[63]:

funcb("food", "upstairs", "rice")


# In[69]:

def funcc(varx, *argv):
#    print(varx)
    for var in argv:
        print(var)


# In[70]:

funcc("food", "upstairs", "rice")


# In[74]:

def funcd(**kwargs):
    for key, value in kwargs.items():
        print("key = %s, \t value = %s" %(key, value))
#        printf("key = %s, \t value = %s", key, value)


# In[75]:

funcd(cusine = "asian", food = "noodles", sauce = "schwz")


# In[79]:

def funce(varx, *args, **kwargs):
    print("varx = ", varx)
    print("--------------")
    for var in args:
        print(var)
    print("--------------")
    for key, value in kwargs.items():
        print("key = %s, \t value = %s" %(key, value))
#        printf("key = %s, \t value = %s", key, value)


# In[81]:

funce(45, 67, "hi", "hello", cusine = "asian", food = ["noodles", "manchurian"], sauce = "schwz")


# In[ ]:



