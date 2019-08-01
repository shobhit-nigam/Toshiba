
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:

matches = pd.read_csv('matches.csv')


# In[3]:

matches.shape


# In[4]:

matches


# In[6]:

matches.info()


# In[7]:

matches.head(5)


# In[8]:

matches['id'].max()


# In[9]:

#matches_2017 = matches

matches['season'].unique()


# In[10]:

matches_2017 = matches[matches['season'] == 2017]


# In[11]:

type(matches)


# In[12]:

type(matches_2017)


# In[13]:

matches_2017.shape[0]


# In[14]:

dfa = matches_2017


# In[15]:

rdfa = dfa[dfa ['winner'] == dfa['toss_winner']]


# In[16]:

rdfa.shape


# In[17]:

perc = (rdfa.shape[0]/dfa.shape[0])*100


# In[18]:

perc


# In[19]:

dfa.tail(1)


# In[20]:

final_2017 = dfa.tail(1)


# In[21]:

final_2017[['team1', 'team2']]


# In[22]:

dl_used = matches[matches['dl_applied'] == 1]


# In[23]:

dl_used


# In[24]:

dl_used.shape[0]


# In[26]:

dl_used['city'].unique()


# In[27]:

dl_used['city'].count()


# In[28]:

dl_used['city'].value_counts()


# In[29]:

dl_used_city = dl_used['city'].value_counts()


# In[30]:

type(dl_used_city)


# In[35]:

sns.countplot(x='city', data=dl_used )
plt.show()


# In[33]:

dl_used_city


# In[36]:

sns.countplot(y='city', data=dl_used )
plt.show()


# In[39]:

matches.tail(4)


# In[40]:

matches.iloc[matches['win_by_runs'].idxmax()]


# In[41]:

matches.iloc[matches['win_by_runs'].idxmax()]['winner']


# In[44]:

matches.iloc[matches[matches['win_by_runs'].ge(1)].win_by_runs.idxmin()]['winner']


# In[45]:

sns.countplot(x='season', data=matches)
plt.show()


# In[46]:

sns.countplot(x='winner', data=matches)
plt.show()


# In[47]:

sns.countplot(y='winner', data=matches)
plt.show()


# In[48]:

data = matches.winner.value_counts()


# In[49]:

data


# In[50]:

sns.countplot(y='player_of_match', data=matches)
top_players = matchesplt.show()


# In[51]:

top_players = matches.player_of_match.value_counts()[:10]


# In[55]:

sns.barplot(y=top_players.index, x=top_players)
plt.show()


# In[ ]:



