
# coding: utf-8

# In[9]:

def taska(varx):
    print("in task A")
    time.sleep(4)
    print("completed task A")


# In[2]:

import time


# In[10]:

def taskb(vary):
    print("in task B")
    time.sleep(6)
    print("completed task B")


# In[6]:

def main():
    print("in main task")
    taska()
    taskb()
    # some activity
    time.sleep(8)
    print("completed task main")


# In[5]:

main()


# In[7]:

main()


# In[8]:

import threading


# In[12]:

def main():
    print("in main task")
    ta = threading.Thread(target=taska, args = (2,))
    tb = threading.Thread(target = taskb, args = (3,))
    ta.start()
    tb.start()
    time.sleep(8)
    print("completed task main")


# In[14]:

main()


# In[17]:

def main():
    print("in main task")
    ta = threading.Thread(target=taska, args = (2,))
    tb = threading.Thread(target = taskb, args = (3,))
    ta.start()
    tb.start()
    time.sleep(2)
    print("completed task main")


# In[18]:

main()


# In[19]:

def main():
    print("in main task")
    ta = threading.Thread(target=taska, args = (2,))
    tb = threading.Thread(target = taskb, args = (3,))
    ta.start()
    tb.start()
    time.sleep(2)
    ta.join()
    tb.join()
    print("completed task main")


# In[20]:

main()


# In[21]:

def taska(varx):
#    print("in task A")
    print("in A thread name = {}".format(threading.current_thread().name))
    print("pid = {}".format(os.getpid()))
    time.sleep(4)
    print("completed task A")


# In[22]:

def taskb(varx):
#    print("in task A")
    print("in B thread name = {}".format(threading.current_thread().name))
    print("pid = {}".format(os.getpid()))
    time.sleep(6)
    print("completed task B")


# In[23]:

import os


# In[24]:

main()


# In[25]:

os.getpid()


# In[26]:

varg = 0


# In[35]:

def funcc():
    global varg
    varg = varg + 1

def taskc(lock):
    for  i in range(1000000):
        lock.acquire()
        funcc()
        lock.release()

def main():
    global varg
    varg = 0
    lock = threading.Lock()
    ta = threading.Thread(target=taskc, args=(lock,))
    tb = threading.Thread(target = taskc, args=(lock,))
    ta.start()
    tb.start()
    ta.join()
    tb.join()


# In[34]:

for i in range(10):
    main()
    print("i = {0} : {1}".format(i, varg))


# In[36]:

for i in range(10):
    main()
    print("i = {0} : {1}".format(i, varg))


# In[37]:

_


# In[38]:

_ = 34


# In[39]:

del _


# In[41]:

print("hi")


# In[42]:

print = 88


# In[43]:

print("hi")


# In[44]:

__builtin__.print("hi")


# In[45]:

del print


# In[46]:

print("hi")


# In[ ]:



