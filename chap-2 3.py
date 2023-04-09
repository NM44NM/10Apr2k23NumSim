# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 23:59:54 2023

@author: 91703_0zbjuu
"""

import numpy as np
y=np.array([[1,4,3],[9,2,7]])
print(y)
print(y[:, [0,2]])
#%%
a=np.arange(1,7)
print(a)
a[1]=1
a[2]=1
a[3]=1
print(a)
#%%
b=np.zeros((2,2))
print(b)
b[0,0]=1
b[0,1]=2
b[1,0]=3
b[1,1]=4
print(b)
#%%
a=np.array([[1,2],[3,4]])
print(a)
a+2
print(a+2)
print(a-2)
print(a**2)
print(b/2)
print(b/5)
print(b//7)
#%%
b=np.array([[1,2],[3,4]])
print(b)
d=np.array([[5,6],[7,8]])
print(d)
print(b*d)
print(b/d)
print(b//d)
print(b.T)
#%%
x = ([[1, 4], [9, 16]])
print(np.sqrt(x))
#%%
x = np.array([1, 2, 4, 5, 9, 3])
if x.all()<3:
    print('yay')
