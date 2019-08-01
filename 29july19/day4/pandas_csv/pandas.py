
# coding: utf-8

# In[1]:

#pandas
import pandas as pd


# In[3]:

food = pd.read_csv('breakfast.csv')


# In[4]:

type(food)


# In[5]:

food.shape


# In[6]:

food


# In[7]:

food.columns


# In[8]:

food.dtypes


# In[9]:

food.columns[0:2]


# In[10]:

food.shape[0]


# In[11]:

dfa = pd.DataFrame({'firm':['toshiba', 'infosys', 'microsoft', 'google', 'cannon'], 'head':['ishikawa', 'bala', 'satya', 'pichai', 'steve'], 'founded':[1985, 1992, 1976, 1994, 1937]})


# In[12]:

dfa


# In[14]:

dfa.index = ['mon', 'tue', 'fri', 'wed', 'thu']


# In[15]:

dfa


# In[16]:

dfa['firm']


# In[19]:

dfa[['firm', 'head']]


# In[20]:

dfa [0:3]


# In[21]:

#loc
#iloc


# In[23]:

dfa.loc[['mon', 'thu']]


# In[24]:

dfa.iloc[3]


# In[26]:

dfa.iloc[3]


# In[27]:

dfa.dtypes


# In[28]:

dfa.set_index('firm')


# In[29]:

dfa.reset_index()


# In[30]:

food


# In[31]:

food.sort_values('Cost')


# In[32]:

#dfa.columns = ['sdfd', 'sdfsd']
dfa.rename(columns={'head':'ceo'})


# In[33]:

#dfa.drop(axis=1, 'ceo')
food['Price']=food.eval('Cost + (Cost*(0.05))')


# In[34]:

food


# In[35]:

food.describe()


# In[37]:

food.isnull().sum()


# In[38]:

food


# In[39]:

dfa


# In[40]:

pd.concat([dfa, food])


# In[41]:

dfa


# In[42]:

food


# In[ ]:



