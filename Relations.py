#!/usr/bin/env python
# coding: utf-8

# In[3]:


def recurrence_relation(n):
    if(n > 0):
        result = n + recurrence_relation(n - 1)
        return result
    else:
        result = 0
        return result
a = int(input("enter the value of n : "))
b = recurrence_relation(a)
print(b)

