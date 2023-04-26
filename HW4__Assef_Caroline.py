#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


integers = np.array ([[1 ,2, 3], [4, 5, 6], [7, 8 ,9],[10, 11,12]])


# In[3]:


integers


# In[4]:


import numpy as np


# In[5]:


integers = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])


# In[6]:


for i in integers.flat:
    print(i, end=" ")


# In[7]:


import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([5, 6, 7, 8, 9, 10])
plt.plot(x, y)
plt.show()


# In[8]:


import matplotlib.pyplot as plt

x = [3, 6, 9, 12]
y = [2, 8, 1, 10]

plt.plot(x, y, marker='o', color='orange')
plt.show()


# In[9]:


import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [2, 4, 6, 14, 10, 12]

plt.plot(x, y, linestyle='dashed', color='b', marker='o', markersize=10, mfc='purple')
plt.show()


# In[10]:


import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([1, 2, 3, 4, 5, 6])
y1 = np.array([5, 6, 7, 8, 9, 10])
x2 = np.array([1, 2, 3, 4, 5, 6])
y2 = np.array([6, 7, 8, 9, 10, 11])
x3 = np.array([1, 2, 3, 4, 5, 6])
y3 = np.array([4, 5, 6, 7, 8, 9])

plt.plot(x1, y1, color='blue')
plt.plot(x2, y2, color='red')
plt.plot(x3, y3, color='green')
plt.show()


# In[11]:


import matplotlib.pyplot as plt
import numpy as np

marks = {'Andy':88, 'Amy':66, 'James':90, 'Jules':55, 'Arthur':77}

plt.bar(marks.keys(), marks.values())
plt.title('student grades')
plt.xlabel('student')
plt.ylabel('grade')


# In[12]:


import matplotlib.pyplot as plt
import numpy as np

marks = {'Andy':88, 'Amy':66, 'James':90, 'Jules':55, 'Arthur':77}

plt.figure(figsize=(8, 6))
mycolors = ["m", "k", "pink", "orange", "blue"]
mylabels= ['andy', 'amy', 'james', 'jules', 'arthur']
myexplode = [0.2, 0, 0, 0, 0]

plt.pie(marks.values(), labels=mylabels, colors=mycolors, explode=myexplode)
plt.title("Student Grades")
plt.legend(title="Students", loc="best")
plt.show()


# In[13]:


import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])

x2 = np.array([0, 1, 2, 3])
y2 = np.array([10, 20, 30, 40])

fig, axs = plt.subplots(2, 3)

axs[0, 0].plot(x1, y1)
axs[0, 0].set_title('Multiple Lines')

axs[0, 1].plot(x2, y2)
axs[0, 1].set_title('Line Plot')

axs[0, 2].scatter(x1, y1)
axs[0, 2].set_title('Scatter Plot')

axs[1, 0].bar(x2, y2)
axs[1, 0].set_title('Bar Chart')

axs[1, 1].pie(y1, labels=x1)
axs[1, 1].set_title('Pie Chart')

axs[1, 2].hist(y2)
axs[1, 2].set_title('Histogram')

plt.tight_layout()
plt.show()


# In[ ]:




