#!/usr/bin/env python
# coding: utf-8

# In[1]:


numbers = list(range(30, 60, 5))


# In[2]:


numbers


# In[3]:


numbers = list(range(30, 60, 5))
print(numbers[::-1])


# In[4]:


nums = list(range(30,70,5))
print(nums[::-1])


# In[5]:


numbers = list(range(20))


# In[6]:


numbers


# In[7]:


del numbers[0]


# In[8]:


numbers


# In[9]:


numbers = list(range(20))
print(max(numbers))
print(min(numbers))


# In[10]:


sum(numbers)


# In[11]:


weather = {"Sunny": "play", "Rainy": "watch TV", "Cloudy": "walk"}

print("Keys\tValues")
for key in weather.keys():
    print(key, "\t", weather[key])


# In[12]:


weather["Snowy"] = "ski"

print("Keys\tValues")
for key in weather.keys():
    print(key, "\t", weather[key])

