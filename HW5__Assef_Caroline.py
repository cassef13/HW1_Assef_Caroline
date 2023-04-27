#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Human:
    def __init__(self, name, age, gender, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation


# In[2]:


A = Human("Alice", 28, "female", "software engineer")
B = Human("Bob", 35, "male", "doctor")


# In[3]:


import math

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)


# In[4]:


p = Point()
print(p.x)
print(p.y)
print(p.distance())


# In[ ]:


(C) When you create an object of B, you have to pass an argument such as B(5). is correct.


# In[6]:


def main():
    print("hello", end="")

if __name__ == "__main__":
    try:
        main()
    except:
        print("name")
    finally:
        print("world")


# In[10]:


class People():
    def __init__(self, name):
        self.name = name
    
    def namePrint(self):
        print(self.name)

person1 = People("Sally")
person2 = People("Louise")
person1.namePrint()


# In[ ]:


(C) 'self' is not needed in def namePrint(self): 
    
    is incorrect about that code


# In[ ]:


TypeError: Only integers are allowed

