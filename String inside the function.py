#!/usr/bin/env python
# coding: utf-8

# In[3]:


def reverse_string(string):

    r_string = ''
    a = len(string)
    while a>0:
        r_string += string[a - 1]
        a = a - 1
    return r_string

print(reverse_string('1234abcd'))


# In[ ]:




