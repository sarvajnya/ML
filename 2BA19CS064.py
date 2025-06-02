
# coding: utf-8

# In[1]:


import numpy as np
                                                                                                                                                                                                                                                                                                                                                                                


# In[2]:


mylist=[10,20,30]
mylist


# In[3]:


print(mylist)


# In[4]:


np.array(mylist)


# In[5]:


mat=[[1,2,3],[4,5,6],[7,8,9]]
mat


# In[6]:


np.array(mat)


# In[7]:


np.arange(0,20)


# In[11]:


np.zeros((5,5))


# In[12]:


np.ones(1)


# In[14]:


np.ones((2,2))


# In[15]:


x=np.zeros(5)
print(x)


# In[17]:


np.linspace(0,20,5)


# In[18]:


print(np.eye(3))


# In[21]:


np.random.rand(10)


# In[25]:


np.random.rand(2,2)


# In[58]:


np.random.rand(5,5)


# In[28]:


np.random.randint(0,5,5)


# In[29]:


arr=np.arange(25)
ranarr=np.random.randint(0,10,25)
print(arr)
print(ranarr)


# In[31]:


arr.reshape(5,5)


# In[32]:


ranarr.reshape(5,5)


# In[37]:


ranarr.argmax()


# In[36]:


arr.max()


# In[38]:


arr.argmax()


# In[39]:


arr.shape


# In[42]:


arr.dtype


# In[43]:


arr[5:8]


# In[44]:


temp=arr.copy()


# In[45]:


temp


# In[46]:


temp[1:8]=99


# In[47]:


temp


# In[48]:


arr


# In[49]:


for i in range(20):
    temp[i]=int(i)
    


# In[50]:


temp


# In[51]:


b=arr>15
b


# In[52]:


arr[b]


# In[53]:


arr


# In[55]:


arr[arr==15]


# In[56]:


x=10
arr[arr>x]


# In[61]:


arr2d=np.random.randint(0,25,25).reshape(5,5)


# In[63]:


arr2d


# In[64]:


arr2d[:2,1:]


# In[65]:


arr2d[2:4,2:4]


# In[66]:


arrt=np.ones((10,10))
arrt


# In[67]:


for i in range(arrt.shape[1]):
    arrt[i]=i


# In[68]:


arrt


# In[73]:


arrt[[2,6,7,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


# In[78]:


arr.shape[0]

