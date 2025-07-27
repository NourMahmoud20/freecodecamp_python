#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
def py_stat(list):
    if len(list)==9:
        dict={}
        a=np.array(list)
        #print(a)
        b=a.reshape(3,3)
        #print(b)
        #print(b.mean(axis=1))
        #print(b.mean(axis=0))
        dict['mean']=[b.mean(axis=1),b.mean(axis=0),b.mean()]
        dict['max']=[b.max(axis=1),b.max(axis=0),b.max()]
        dict['min']=[b.min(axis=1),b.min(axis=0),b.min()]
        dict['std']=[b.std(axis=1),b.std(axis=0),b.std()]
        dict['var']=[b.var(axis=1),b.var(axis=0),b.var()]
        dict['sum']=[b.sum(axis=1),b.sum(axis=0),b.sum()]
        #print(dict)
        return dict
    
print(py_stat([0,1,2,3,4,5,6,7,8]))

