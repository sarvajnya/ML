
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
labels=['a','b','c']
my_list=[10,20,30]
arr=np.array([10,20,30])
d={'a':10,'b':20,'c':30}


# In[5]:


pd.Series(data=my_list)


# In[6]:


pd.Series(data=my_list,index=labels)


# In[7]:


pd.Series(my_list,labels)


# In[8]:


pd.Series(arr)


# In[9]:


pd.Series(arr,labels)


# In[10]:


pd.Series(d)


# In[11]:


pd.Series(data=labels)


# In[12]:


pd.Series([sum,print,len])


# In[13]:


s1=pd.Series([1,2,3,4],index=['usa','japan','india','ussr'])


# In[14]:


s1


# In[15]:


s2=pd.Series([1,2,3,4],index=['usa','germany','india','brazil'])


# In[16]:


s2


# In[17]:


s1['usa']


# In[18]:


s1+s2

