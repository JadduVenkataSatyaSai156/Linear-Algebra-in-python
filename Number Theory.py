#!/usr/bin/env python
# coding: utf-8

# In[1]:


# python program for generating fibonacci sequence based on user input for number of terms
# user input for number of terms of a sequence and store it in n
n = int(input("enter number of terms : "))
# initialize a as 0
a = 0
# initialize b as 1
b = 1
# for loop on checking everyhting term
for i in range(n):
    # print a
    print(a)
    # make transfer values of b to a
    a = b
    # transfer sum of and b and transfer to b
    b = a + b

