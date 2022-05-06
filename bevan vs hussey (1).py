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


df = pd.read_csv('ODI_data.csv')


# In[3]:


df.head()


# In[4]:


# runs per innings
# sr
# 100's
# 50's
# team contri


# In[5]:


df['Innings Runs Scored Num'].unique()


# In[6]:


df = df[df["Innings Runs Scored Num"] != '-']


# In[7]:


df = df.dropna(subset = ['Innings Runs Scored Num'])


# In[8]:


df['Innings Runs Scored Num'].unique()


# In[9]:


# convert to datetime
df['Innings Date'] = pd.to_datetime(df['Innings Date'])


# In[10]:


df['year'] = df['Innings Date'].dt.year


# In[11]:


df.tail(1)


# In[12]:


df['Innings Runs Scored Num'] = df['Innings Runs Scored Num'].astype('int')


# In[13]:


df['Innings Balls Faced'] = df['Innings Balls Faced'].astype('int')


# In[14]:


df['Innings Not Out Flag'] = df['Innings Not Out Flag'].astype('int')


# In[15]:


# Bevan 1998 - 2006
# Hussey 2004 - 2012


# In[16]:


bevan_df = df[(df.year >= 1996) & (df.year <= 2004)]


# In[17]:


hussey_df = df[(df.year >= 2004) & (df.year <= 2012)]


# In[18]:


bevan_df.tail()


# In[19]:


hussey_df.tail()


# In[20]:


# runs per innings = total runs/Total Innings
# sr = 100*(total runs/balls)
# 100's = sum
# 50's = sum
# team contribution = player runs/team runs


# In[21]:


df.dtypes


# In[22]:


bevan_df.tail(200)


# In[23]:


# MG Bevan
bdf = bevan_df[bevan_df['Innings Player'] == 'MG Bevan']


# In[24]:


bdf.tail()


# In[25]:


hussey_df.head(200)


# In[26]:


# MEK Hussey
mkf = hussey_df[hussey_df['Innings Player'] == 'MEK Hussey']


# In[27]:


mkf.head()


# In[28]:


sum(bdf['Innings Runs Scored Num'])


# In[29]:


sum(mkf['Innings Runs Scored Num'])


# In[30]:


len(bdf), len(mkf)


# In[31]:


# rpi - bevan, hussey
sum(bdf['Innings Runs Scored Num'])/len(bdf), sum(mkf['Innings Runs Scored Num'])/len(mkf)


# In[32]:


# sr
100*sum(bdf['Innings Runs Scored Num'])/sum(bdf['Innings Balls Faced']), 100*sum(mkf['Innings Runs Scored Num'])/sum(mkf['Innings Balls Faced'])


# In[33]:


# 100's
sum(bdf["100's"]), sum(mkf["100's"])


# In[34]:


# 50's
sum(bdf["50's"]), sum(mkf["50's"])


# In[35]:


# team contri - runs by each player,runs by team
sum(bdf['Innings Runs Scored Num']), sum(mkf['Innings Runs Scored Num'])


# In[36]:


# 1998-2006 = all players
sum(bevan_df[bevan_df.Country == 'Australia']['Innings Runs Scored Num'])


# In[37]:


# 1998-2006 = all players
sum(hussey_df[hussey_df.Country == "Australia"]['Innings Runs Scored Num'])


# In[38]:


100*sum(bdf['Innings Runs Scored Num'])/sum(bevan_df[bevan_df.Country == 'Australia']['Innings Runs Scored Num'])


# In[39]:


100*sum(mkf['Innings Runs Scored Num'])/sum(hussey_df[hussey_df.Country == "Australia"]['Innings Runs Scored Num'])


# In[40]:


bevan_df.groupby(['Innings Player'])['Innings Runs Scored Num'].sum().sort_values(ascending = False).head(30).plot(kind = 'barh')


# In[41]:


hussey_df.groupby(['Innings Player'])['Innings Runs Scored Num'].sum().sort_values(ascending = False).head(30)


# In[42]:


bdf.groupby(['year'])['Innings Runs Scored Num'].sum()


# In[43]:


mkf.groupby(['year'])['Innings Runs Scored Num'].sum()


# In[45]:





# In[46]:





# In[49]:


# Innings Balls Faced
100*sum(mkf['Innings Runs Scored Num'])/sum(mkf['Innings Balls Faced'])


# In[50]:


# players runs excluding bevan =>not bevan = bevan_df[bevan_df.player_name != 'MG Bevan']


# In[52]:


# rpi - bevan, hussey
sum(bevan_df['Innings Runs Scored Num'])/len(bevan_df), sum(hussey_df['Innings Runs Scored Num'])/len(hussey_df)


# In[53]:


non_bevan_df = bevan_df[bevan_df['Innings Player'] != 'MG Bevan']


# In[55]:


(sum(bdf['Innings Runs Scored Num'])/len(bdf))/(sum(non_bevan_df['Innings Runs Scored Num'])/len(non_bevan_df))


# In[56]:


non_hussey_df = hussey_df[hussey_df['Innings Player'] != 'MEK Hussey']


# In[57]:


(sum(mkf['Innings Runs Scored Num'])/len(mkf))/(sum(non_hussey_df['Innings Runs Scored Num'])/len(non_hussey_df))


# In[63]:


non_hussey_df.head()


# In[64]:


len(bdf), len(mkf)


# In[65]:


180/6, 157/3


# In[66]:


45/180, 39/157


# In[ ]:




