
# coding: utf-8

# In[1]:

print(varx)


# In[3]:

lista = []
listb = [7, 3, 10]


# In[4]:

avg = sum(listb)/len(listb)


# In[5]:

avg


# In[6]:

avg = sum(lista)/len(lista)


# In[7]:

try:
    avg = sum(lista)/len(lista)
    print(avg)
except ZeroDivisionError:
    print('list is empty')


# In[8]:

try:
    avg = sum(listc)/len(lista)
    print(avg)
except ZeroDivisionError:
    print('list is empty')


# In[10]:

try:
    avg = sum(listc)/len(lista)
    print(avg)
except ZeroDivisionError:
    print('list is empty')
except NameError:
    print('name went wrong')


# In[11]:

try:
    index = int(input())
    avg = sum(listb)/len(listb)
    print(avg)
    print(listb[index])
except ZeroDivisionError:
    print('list is empty')
except NameError:
    print('name went wrong')
    


# In[12]:

listb


# In[13]:

try:
    index = int(input())
    avg = sum(listb)/len(listb)
    print(avg)
    print(listb[index])
except ZeroDivisionError:
    print('list is empty')
except NameError:
    print('name went wrong')
    


# In[15]:

try:
    index = int(input())
    avg = sum(listb)/len(listb)
    print(avg)
    print(listb[index])
except ZeroDivisionError:
    print('list is empty')
except NameError:
    print('name went wrong')
except:
    print("something went wrong, dont't know what")


# In[18]:

try:
    try:
        index = int(input())
        avg = sum(listb)/len(listb)
        print(avg)
        print(listb[index])
    except ZeroDivisionError:
        print('inner block')
except ZeroDivisionError:
    print('list is empty')
except NameError:
    print('name went wrong')
except:
    print("something went wrong, dont't know what")


# In[22]:

def funca():
    try:
        inta = 20
        intb = 0
        avg = inta/intb
        print(avg)
    except NameError:
        print("you have type the spelling wrong")


# In[23]:

funca()


# In[24]:

try:
    funca()
except:
    print('something wrong')


# In[25]:

lista = [3, 7, 10, 5]

try:
    n = int(input())
    if n <= 0:
        raise ValueError('not a positive num')
    else:
        print(lista[n])
except ValueError as obj:
    print(obj)


# In[26]:

lista = [3, 7, 10, 5]

try:
    n = int(input())
    if n <= 0:
        raise ValueError('not a positive num')
    else:
        print(lista[n])
except ValueError as obj:
    print(obj)


# In[28]:

class AppException(Exception):
    pass

class ValueLarge(AppException):
    """ value too large """
    pass

class ValueSmall(AppException):
    """ value too small"""
    pass


# In[29]:

number = 10

while True:
    try:
        i_num = int(input("enter a num:"))
        if i_num < number:
            raise ValueSmall
        elif i_num > number:
            raise ValueLarge
        else:
            break
    except ValueSmall:
        print(ValueSmall.__doc__)
        print('try again')
    except ValueLarge:
        print(ValueLarge.__doc__)
        print('try again')

print('congrats, you guessed correctly')


# In[ ]:



