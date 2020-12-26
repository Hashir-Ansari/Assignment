#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[2]:


import numpy as np


# In[3]:


x=np.array([0,1,2,3,4,5,6,7,8,9])
x


# In[4]:


x.ndim


# In[5]:


x=np.reshape(x,(2,5))
x


# In[6]:


x.ndim


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[7]:


a=np.array([0,1,2,3,4,5,6,7,8,9])
b=np.array([10,11,12,13,14,15,16,17,18,19])


# In[8]:


a=np.reshape(a,(2,5))
b=np.reshape(b,(2,5))


# In[9]:


np.vstack((a,b))


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[10]:


x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([10,11,12,13,14,15,16,17,18,19])


# In[11]:


np.vstack((x,y))


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[12]:


f=np.vstack((a,b))

np.ravel(f)


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[13]:


np.array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]]).ravel()


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[14]:


np.array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]).reshape(5,3)


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[15]:


x=np.random.randn(25).reshape(5,5)*5
np.array(x)
x=np.square(x)
x


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[16]:


x=np.random.randn(25).reshape(5,5)*5
x=np.array(x)
m=np.mean(x)
m


# In[17]:


x


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[18]:


np.std(x)


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[19]:


np.median(x)


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[20]:


x


# In[21]:


x.T


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[22]:


x=np.random.randn(16).reshape(4,4)*5
x=np.array(x)
x


# In[23]:


np.diagonal(x)


# In[24]:


np.diagonal(x).sum()


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[25]:


x


# In[26]:


x.shape


# In[27]:


np.linalg.det(x)


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[28]:


x


# In[29]:


print("5th percentile",np.percentile(x, 5))
print("95th percentile",np.percentile(x, 95))


# ## Question:15

# ### How to find if a given array has any null values?

# In[30]:


b = np.arange(25).reshape(5, 5) 
                 
print("\nIs NaN: \n", np.isnan(b)) 
    
c = [[1,2,3],  
     [np.nan,2,2]] 
print("\nIs NaN: \n", np.isnan(c))


# In[ ]:




