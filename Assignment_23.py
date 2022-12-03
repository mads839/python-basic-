#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1. What is the result of the code, and why?
def func(a, b=6, c=8):
    print(a, b, c)
func(1, 2)

#as value of C not given so it will automatically take default value


# In[2]:


#2. What is the result of this code, and why?
def func(a, b, c=5):
    print(a, b, c)
func(1, c=3, b=2)

#value of a is not assign so it will take 1 as default value


# In[4]:


#How about this code: what is its result, and why?
def func(a, *pargs):
    print(a, pargs)
func(1, 2, 3)
#* a single asterisk (*) to unpack iterables.Here 1 will assign to first positional variable a,
#so all other values are packed second positional pargs


# In[5]:


#4.What does this code print, and why?
def func(a, **kargs):
    print(a, kargs)
func(a=1, c=3, b=2)
#* a single asterisk (**) to unpack dictionaries.Here 1 will assign to first positional variable a,
#so all other values are packed second keyword argument as dicionaries.


# In[10]:


#What gets printed by this, and explain?
def func(a, b, c=8, d=5):
    print(a, b, c, d)
func(1, *(5, 6))

#* a single asterisk (*) to unpack iterables so after unpacking b,c will take value 5,6 
#and value of d will automatically take 5


# In[22]:


#what is the result of this, and explain?
def func(a, b, c): 
    a = 2; b[0] = 'x'; c['a'] = 'y'
    l=1; m=[1]; n={'a':0}
    
func(l,m,n)



# In[ ]:




