#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[5]:


labels=['a','b','c']
my_data=[10,20,30]
arr =np.array(my_data)
d = {'a':10,'b':20,'c':30}


# In[6]:


pd.Series(data=my_data)


# In[7]:


pd.Series(my_data,labels)


# In[8]:


ser1 =pd.Series([1,2,3,4],['USA','GERMANY','USSR','JAPAN'])


# In[9]:


ser1


# In[10]:


ser2=pd.Series([1,2,4,6],['USA','GERMANY','INDIA','JAPAN'])


# In[11]:


ser3=ser1+ser2


# In[12]:


ser3


# In[13]:


from numpy.random import randn


# In[14]:


np.random.seed(101)


# In[15]:


df =pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[16]:


df


# In[17]:


df['W']


# In[18]:


df[['W','Z']]


# In[19]:


type(df)


# In[20]:


df['new'] = df['W']*df['Y']


# In[21]:


df


# In[22]:


df.drop('new',axis=1,inplace=True)


# In[23]:


df


# In[24]:


df.drop('E')


# In[25]:


df.drop('E',axis=0)


# In[26]:


df.shape


# In[27]:


df.loc[['A','B'],['W','Y']]


# In[28]:


df


# In[30]:


df[df['W']>0]


# In[31]:


df.reset_index()


# In[32]:


newwind='CA NY WY OR CO'.split()


# In[33]:


df['States']=newwind


# In[34]:


df


# In[36]:


df.set_index('States',inplace=True)


# In[37]:


df


# In[38]:


outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[40]:


df=pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
df


# In[41]:


df.loc['G1'].loc[1]


# In[42]:


df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})


# In[43]:


df


# In[44]:


df.dropna()


# In[45]:


df.dropna(axis=1)


# In[47]:


df.dropna(thresh=2)


# In[48]:


df.fillna(value='Anmol')


# In[56]:


df['A'].fillna(value=df['C'].mean())


# In[57]:


data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}


# In[58]:


df=pd.DataFrame(data)


# In[60]:


df


# In[61]:


df.groupby('Company')


# In[62]:


by_comp=df.groupby('Company')


# In[63]:


by_comp.mean()


# In[64]:


df.groupby('Company').mean()


# In[65]:


by_comp.std()


# In[66]:


by_comp.min()


# In[67]:


by_comp.max()


# In[68]:


by_comp.describe()


# In[72]:


by_comp.describe().transpose()['FB']


# In[ ]:




