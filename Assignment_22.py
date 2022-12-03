#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. What is the result of the code, and explain?
X = 'iNeuron'
def func():
    print(X)
func()

#iNeuron

#print function inside func() will print"iNeuron"


# In[4]:


#2. What is the result of the code, and explain?

X = 'iNeuron'
def func():
    X = 'NI!'

func()
print(X)

#iNeuron


#print function is  out of func() so it will print"iNeuron"


# In[6]:


#3.What does this code print, and why?
X = 'iNeuron'
def func():
    X = 'NI'
print(X)

func()
print(X)

#iNeuron
#iNeuron


#here both print function inside and outside of func() will print "iNeuron"


# In[7]:


#4. What output does this code produce? Why?

X = 'iNeuron'
def func():
    global X
    X = 'NI'
func()
print(X)

#NI


# here X is global variable so print function out of func() also print "NI"


# In[15]:


#5.What about this code—what’s the output, and why?
X = 'iNeuron'
def func():
    X = 'NI'
def nested():
    print(X)
    nested()
func()
X
#'iNeuron'


# In[16]:


#6. How about this code: what is its output in Python 3, and explain?
def func():
    X = 'NI'
    def nested():
        nonlocal X
        X = 'Spam'
        nested()
    print(X)
func()




#NI


# In[ ]:




