#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# to display all columns and row
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth',-1)


# In[2]:


# ipl ball by ball data


# In[3]:


df = pd.read_csv('ipl_ball_by_ball_data.csv')


# In[4]:


df.head(10)


# In[5]:


df.innings.unique()


# In[6]:


df = df[(df.innings == 1) | (df.innings == 2)]


# In[7]:


df.innings.unique()


# In[8]:


# what are the numbers when russell faces rashid
# filter by player names
# use the names and assign it to striker and bolwer
#  get the required columns


# In[9]:


df.bowling_team.unique()


# In[10]:


df[df.bowling_team == 'Sunrisers Hyderabad']['bowler'].unique()
# Sandeep Sharma


# In[11]:


df[df.batting_team == 'Royal Challengers Bangalore']['striker'].unique()
# V Kohli


# In[12]:


req_df = df[(df.striker == 'V Kohli') & (df.bowler == 'Sandeep Sharma')]


# In[13]:


req_df.head()  


# In[14]:


len(req_df)


# In[15]:


# no of runs
# no of balls
# no of wickets


# In[16]:


req_df.runs_off_bat


# In[17]:


req_df.runs_off_bat.sum()


# In[18]:


# outs
req_df[req_df.player_dismissed == 'V Kohli']


# In[19]:


# strike rate
100*sum(req_df.runs_off_bat/len(req_df))


# In[20]:


# comparison against all batsman sandeep has bowled to


# In[21]:


sandeep_df = df[df.bowler == 'Sandeep Sharma']


# In[22]:


sandeep_df.head()


# In[23]:


# runs scored by this batsman
sdf1 = pd.DataFrame(sandeep_df.groupby('striker')['runs_off_bat'].sum()).reset_index()


# In[24]:


sdf2 = pd.DataFrame(sandeep_df.groupby('striker')['ball'].count()).reset_index()


# In[55]:


sdf1.head()


# In[25]:


sdf2.head()


# In[26]:


sdf3 = sdf1.merge(sdf2, on ='striker', how = 'left')


# In[27]:


sdf3.head()


# In[28]:


sdf3['strike_rate'] = 100*sdf3['runs_off_bat']/sdf3['ball']


# In[29]:


sdf3.head()


# In[30]:


# min criteria of 30 balls


# In[31]:


sdf3 = sdf3[sdf3.ball >= 30]


# In[32]:


sdf3.head(30)


# In[33]:


v_df = df[df.striker == 'V Kohli']


# In[34]:


# runs scored by this batsman
v_df1 = pd.DataFrame(v_df.groupby('bowler')['runs_off_bat'].sum()).reset_index()


# In[35]:


v_df1.head()


# In[36]:


v_df2 = pd.DataFrame(v_df.groupby('bowler')['ball'].count()).reset_index()


# In[37]:


v_df2.head()


# In[38]:


v_df3 = v_df1.merge(v_df2, on = 'bowler', how = 'left')


# In[39]:


v_df3.head()


# In[40]:


v_df3['strike_rate'] = 100*v_df3['runs_off_bat']/v_df3['ball']


# In[41]:


v_df3.head()


# In[42]:


# min criteria 30 balls


# In[43]:


v_df3 = v_df3[v_df3.ball >= 50]


# In[44]:


sdf3.reset_index(inplace = True, drop = True)
v_df3.reset_index(inplace = True, drop = True)


# In[45]:


sdf3.head(30)


# In[46]:


sdf3.sort_values('strike_rate', ascending = False)


# In[47]:


v_df3.sort_values('strike_rate', ascending = False)


# In[54]:


plt.figure(figsize = (14, 10))
plt.scatter(v_df3.strike_rate, v_df3.ball)
for i in range(len(v_df3)):
    if v_df3['bowler'][i] == 'Sandeep Sharma':
        plt.text(v_df3['strike_rate'][i] -2, v_df3['ball'][i] -1, v_df3['bowler'][i])
    else:
        plt.text(v_df3['strike_rate'][i] +2, v_df3['ball'][i] -1, v_df3['bowler'][i])
plt.axvline(125, ls = '--', color = 'grey')
plt.axhline(65, ls = '--', color = 'grey')
plt.title('Virat against all Bowlers in IPL( min 30 balls)', fontsize = 10)
plt.xlabel('Strike Rate')
plt.ylabel('Ball')
plt.show()


# In[52]:


plt.figure(figsize = (14, 8))
plt.scatter(sdf3.strike_rate, sdf3.runs_off_bat)
for i in range(len(sdf3)):
#     plt.text(x, y, text)
    if sdf3['striker'][i] =='S Dhawan':
        plt.text(sdf3['strike_rate'][i] -12, sdf3['runs_off_bat'][i] -1, sdf3['striker'][i] )
    else:
        plt.text(sdf3['strike_rate'][i] +1, sdf3['runs_off_bat'][i] -1, sdf3['striker'][i] )
plt.axvline(121, ls = '--', color = 'yellow')
plt.axhline(55,ls = '--', color = 'blue')
plt.title('Batsman against sandeep in IPL (min 30 balls faced)', fontsize = 10)
plt.xlabel('Strike Rate')
plt.ylabel('Runs Scored')
plt.show()


# In[ ]:




