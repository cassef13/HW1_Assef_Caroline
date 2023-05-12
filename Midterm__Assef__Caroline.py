#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import json

list1=[2,4,6,8,4,5,2,1,9,0,4,6,7,4,3,2,1,9,10,3,7,9,6,0,1,3,5,6,7,8,9,10,2,3,6,8,9,10,6,7,4,3]
dict1={}

for i in list1:
    if i not in dict1: 
        dict1[i]=1
    else:
        dict1[i]+=1    
        

list2=sorted(dict1.items())
for i in list2:
    print(i[0],":",i[1])
    

plt.bar(list(dict1.keys()), dict1.values(), color='b')
plt.show()


with open('frequency.json', 'w') as f:
    json.dump(dict1,f)


# In[2]:


import pandas as pd


# In[3]:


df = pd.read_json('your_posts_1.json')


# In[4]:


df.head(10)


# In[5]:



df.rename(columns={'timestamp': 'date'}, inplace=True)


df = df.drop(['attachments', 'title'], axis=1)


pd.to_datetime(df['date'])

df.head(3)


# In[6]:


print(df.shape)
df.tail(3)


# In[7]:


monthly_summary = df.resample('M', on='date').size()
print(monthly_summary)

average = df['date'].mean()
median = df['date'].median()
maximum = df['date'].max()
minimum = df['date'].min()
std_deviation = df['date'].std()


# In[ ]:


print("Average:", average)
print("Median:", median)
print("Max:", maximum)
print("Min:", minimum)
print("Standard Deviation:", std_deviation)


# In[8]:





# In[9]:


# Pie Chart
labels = list(dict1.keys())
sizes = list(dict1.values())


# In[10]:


plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()


# In[11]:


# Bar Chart
plt.bar(list(dict1.keys()), dict1.values(), color='purple')
plt.show()


# In[12]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range(start=minimum, end=maximum, freq='D')
counts = df.groupby(df['date'].dt.date).size()

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(counts.index, counts.values, label='Posts')
ax.plot(counts.index, np.cumsum(counts.values), label='Cumulative Posts')
ax.plot(monthly_summary.index, monthly_summary.values, label='Monthly Posts')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Posts')
ax.legend()
plt.show()


# In[ ]:




