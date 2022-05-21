#!/usr/bin/env python
# coding: utf-8

# # Pandas 2

# In[8]:


import pandas as pd

df=pd.read_csv("empl.csv")
print (df)


# In[9]:


import pandas as pd

df=pd.read_csv("https://raw.githubusercontent.com/dsrscientist/dataset1/master/empl.csv")
print (df)


# In[12]:



df=pd.read_csv("empl.csv",index_col=['SNo'])
print (df)


# In[17]:


import numpy as np

df=pd.read_csv('empl.csv', dtype={'Salary':np.float64})

print(df.dtypes)
df


# In[19]:


df['Salary'].max()


# In[20]:


df['Salary'].min()


# In[21]:


df['Salary'].plot()


# In[23]:


#location based operation

df.loc[:,'Salary']


# In[25]:


df1=pd.DataFrame(data=df)
df1


# In[26]:


df.loc[:,'Salary']


# In[27]:


df.loc[:,['Name','Salary']]


# In[28]:


df1.iloc[:,0:4]


# In[31]:


df1.iloc[:,-3:-2]


# In[32]:


df1.iloc[:,-4:-1]


# In[33]:


df.count()


# In[34]:


df['Name'].count()


# In[36]:


df1['Name'].unique()


# In[37]:


df1['Name'].nunique()


# In[41]:


print(df1['Name'].describe())


# In[42]:


df1.describe()


# In[44]:


df1.describe(include='all')


# Dropping of Rows and Columns in Pandas

# In[45]:


df1


# In[47]:


df1.columns


# In[48]:


df2=df1.drop([14,15,16,17],axis=0)


# In[50]:


df2


# In[51]:


df1.drop([1,2,3],inplace=True,axis=0)
df1


# In[52]:


df2


# In[53]:


df3=df1.drop('Name',axis=1)


# In[54]:


df3


# # Data Munging

# In[58]:


import pandas as pd
country=pd.read_csv('empl.csv',index_col=0)
country.to_html('emp1test.html')


# In[ ]:




