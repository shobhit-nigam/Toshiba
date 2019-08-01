
# coding: utf-8

# In[1]:

import time

def taska():
    for i in range(3, 0, -1):
        print(i, 'seconds left')
        time.sleep(1)


# In[2]:

taska()


# In[3]:

import time

def taska():
    for i in range(3, 0, -1):
        print(i, 'seconds left in A')
        time.sleep(1)

def taskb():
    for i in range(6, 0, -1):
        print(i, 'seconds left in B')
        time.sleep(1)

def maintask():
    taska()
    taskb()
    for i in range(9, 0, -1):
        print(i, 'seconds left in main task')
        time.sleep(1)  
    print('exiting main')


# In[4]:

maintask()


# In[5]:

import threading 

def maintask():
    ta = threading.Thread(target=taska)
    tb = threading.Thread(target=taskb) 
    ta.start()
    tb.start()
    for i in range(9, 0, -1):
        print(i, 'seconds left in main task')
        time.sleep(1)  
    print('exiting main')


# In[6]:

maintask()


# In[7]:

maintask()


# In[10]:

import time
import threading

def taska():
    for i in range(9, 0, -1):
        print(i, 'seconds left in A')
        time.sleep(1)

def taskb():
    for i in range(3, 0, -1):
        print(i, 'seconds left in B')
        time.sleep(1)

def maintask():
    ta = threading.Thread(target=taska)
    tb = threading.Thread(target=taskb) 
    ta.start()
    tb.start()
    for i in range(6, 0, -1):
        print(i, 'seconds left in main task')
        time.sleep(1)  
    ta.join()
    tb.join()
    print('exiting main')


# In[11]:

maintask()


# In[12]:

import time
import threading

def taska():
    for i in range(9, 0, -1):
        print(i, 'seconds left in A')
        time.sleep(1)

def taskb():
    for i in range(3, 0, -1):
        print(i, 'seconds left in B')
        time.sleep(1)

def maintask():
    ta = threading.Thread(target=taska, args=(10,))
    tb = threading.Thread(target=taskb) 
    ta.start()
    tb.start()
    for i in range(6, 0, -1):
        print(i, 'seconds left in main task')
        time.sleep(1)  
    ta.join()
    tb.join()
    print('exiting main')


# In[21]:

x = 0

def funca():
    pass

def taskc():
    global x
    x = x+1
    print('\ntask {} is starting'.format(x))
    for i in range(10000):
        funca()
        pass
    print('\ntask {} is ending'.format(x))    

def maintask():
    ta = threading.Thread(target=taskc)
    tb = threading.Thread(target=taskc) 
    ta.start()
    tb.start()
    ta.join()
    tb.join()

maintask()


# In[15]:

maintask()


# In[25]:

x = 0

def funca():
    pass

def taskc():
    global x
    x = x+1
    print('\ntask {} is starting'.format(x))
    for i in range(1000000):
        funca()
        pass
    print('\ntask {} is ending'.format(x))    

def maintask():
    ta = threading.Thread(target=taskc)
    tb = threading.Thread(target=taskc) 
    ta.start()
    tb.start()
    ta.join()
    tb.join()

maintask()


# In[28]:

x = 0

lock = threading.Lock()
def funca():
    pass

def taskc():
    global x
    lock.acquire()
    x = x+1
    print('\ntask {} is starting'.format(x))
    for i in range(1000000):
        funca()
        pass
    print('\ntask {} is ending'.format(x)) 
    lock.release()

def maintask():
    ta = threading.Thread(target=taskc)
    tb = threading.Thread(target=taskc) 
    ta.start()
    tb.start()
    ta.join()
    tb.join()

maintask()


# In[ ]:



