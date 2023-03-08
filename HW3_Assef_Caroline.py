#!/usr/bin/env python
# coding: utf-8

# In[1]:


marks = {'Andy': 88, 'Amy': 66, 'James': 90, 'Jules': 55, 'Arthur': 77}

def get_grade(student_name):
    if student_name in marks:
        return marks[student_name]
    else:
        print("You cannot find this student's name.")

print(get_grade('Andy'))  
print(get_grade('Sarah'))


# In[2]:


marks = {'Andy': 88, 'Amy': 66, 'James': 90, 'Jules': 55, 'Arthur': 77}

def get_average_grade():
    total_grades = 0
    num_students = len(marks)
    
    for grade in marks.values():
        total_grades += grade
    
    return total_grades / num_students


print(get_average_grade())


# In[3]:


def print_squares(num):
    n = 0
    while n < num:
        print(n, n**2)
        n += 1
    else:
        print("greater than", num)

print_squares(8)


# In[4]:


def sum_to_num(num):
    n = 1
    sum = 0
    
    while n <= num:
        sum += n
        n += 1
    
    print("The sum of integers from 1 to", num, "is:", sum)

sum_to_num(10)


# In[5]:


def sum_to_num(num):
    sum = 0
    
    for n in range(1, num+1):
        sum += n
        print("sum after adding", n, "is:", sum)

sum_to_num(5)


# In[6]:


import statistics

def calculate_stats(lst):
    mean = statistics.mean(lst)
    total = sum(lst)
    stdev = statistics.stdev(lst)
    
    print("The mean is:", mean)
    print("The sum is:", total)
    print("The standard deviation is:", stdev)

lst = list(range(1, 101))
calculate_stats(lst)


# In[7]:


def minimal(v1, v2, v3, v4):
    
    min_val = v1
    
  
    if v2 < min_val:
        min_val = v2
        
    if v3 < min_val:
        min_val = v3
        
    if v4 < min_val:
        min_val = v4
        
  
    return min_val


result = minimal(9, 3, 6, 2)
print("The minimal value is:", result)


# In[8]:


def concatenate_strings(str1, str2, str3):
    concatenated_string = str1 + str2 + str3
    return concatenated_string

string1 = "Hello, "
string2 = "how "
string3 = "are you?"
result = concatenate_strings(string1, string2, string3)
print(result)


# In[ ]:




