
# coding: utf-8

# In[1]:

from matplotlib import pyplot as plt
from matplotlib import style


# In[2]:

lista = [6, 9, 11]
listb = [11, 15, 7]

listc


# In[3]:

plt.plot(lista, listb)


# In[4]:

plt.show()


# In[7]:

plt.plot(lista, listb, linewidth=4, color ='r' )
plt.show()


# In[8]:

lista = [6, 9, 11]
listb = [11, 15, 7]

listc = [6, 10, 13]
listd = [6, 16, 8]


# In[9]:

plt.plot(lista, listb, linewidth=2, color ='r' )
plt.plot(listc, listd, linewidth=2, color ='g' )
plt.show()


# In[11]:

plt.plot(lista, listb, linewidth=2, color ='r', label='actual' )
plt.plot(listc, listd, linewidth=2, color ='g', label = 'expected' )
plt.legend()
plt.show()


# In[12]:

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

lista = [6, 9, 11]
listb = [11, 15, 7]

listc = [6, 10, 13]
listd = [6, 16, 8]
plt.plot(lista, listb, linewidth=2, color ='r', label='actual' )
plt.plot(listc, listd, linewidth=2, color ='g', label = 'expected' )
plt.legend()
plt.show()


# In[15]:

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

lista = [6, 9, 11]
listb = [11, 15, 7]

listc = [6, 10, 13]
listd = [6, 16, 8]

plt.bar(lista, listb)
plt.bar(listc, listd)
plt.show()


# In[16]:

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

lista = [6, 9, 11]
listb = [11, 15, 7]

listc = [6, 10, 13]
listd = [6, 16, 8]

plt.scatter(lista, listb)
plt.scatter(listc, listd)
plt.show()


# In[18]:

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

lista , listb = np.loadtxt('val.csv', delimiter = ',', unpack= True)

plt.plot(lista, listb)
plt.show()


# In[ ]:



