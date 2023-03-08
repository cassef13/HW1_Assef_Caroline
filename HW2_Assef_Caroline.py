#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = 0

while n < 10:
    if n == 5:
        break
    print(n)
    n += 1


# In[2]:


n = 0

while n < 5:
    print(n)
    n += 1

if n >= 5:
    print(f"{n} is not less than 5")


# In[3]:


fruits = ["bananas", "peaches", "apples", "grapes", "mangos"]
output = ""

for fruit in fruits:
    output += f"i like {fruit}. "
    if fruit == "apples":
        output += "are apples fruits?"
        break

print(output)


# In[4]:


n = 1
total = 0

while n <= 30:
    total += n
    n += 1

print("The sum of integers from 1 to 30 is:", total)


# In[5]:


score = 55

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("The student's grade is:", grade)


# In[6]:


marks = {'Andy':88, 'Amy':66, 'James':90, 'Jules':55, 'Arthur':77}

def numeric_to_letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

letter_grades = {name: numeric_to_letter_grade(grade) for name, grade in marks.items()}

print("The dictionary of student letter grades is:", letter_grades)


# In[7]:


marks = {'Andy':88, 'Amy':66, 'James':90, 'Jules':55, 'Arthur':77}

for name, grade in marks.items():
    print(name, "got a grade of", grade)


# In[8]:


marks = {'Andy':88, 'Amy':66, 'James':90, 'Jules':55, 'Arthur':77}

grades = list(marks.values())
mean_grade = sum(grades) / len(grades)
max_grade = max(grades)
min_grade = min(grades)

print("Mean grade:", mean_grade)
print("Maximum grade:", max_grade)
print("Minimum grade:", min_grade)


# In[9]:


marks = {'Andy':88, 'Amy':66, 'James':90, 'Jules':55, 'Arthur':77}

for key in marks.keys():
    if 'J' in key:
        break
    print(key)


# In[10]:


marks = {'Andy':88, 'Amy':66, 'James':90, 'Jules':55, 'Arthur':77}

for key in marks.keys():
    if 'J' in key:
        continue
    print(key)


# In[ ]:




