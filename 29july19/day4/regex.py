
# coding: utf-8

# In[1]:

#        ^a..a$
#    asia
#    america


# In[2]:

import re


# In[6]:

pattern = '^a..a$'
stringa = input()
result = re.match(pattern, stringa)
if result:
    print('its a match')
else:
    print('not a match')


# In[7]:

pattern = 'h..l'
stringa = input()

result = re.findall(pattern, stringa)
print(result)


# In[8]:

#     ^  $  []   .   *   {}    +   ?   


# In[ ]:

#    []
#https://www.programiz.com/python-programming/regex

