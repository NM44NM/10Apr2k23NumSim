# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 00:35:23 2023

@author: 91703_0zbjuu
"""
import numpy as np
from numpy.linalg import qr
a = np.array([[0, 2], 
              [2, 3]])
q, r = qr(a)
print('Q:', q)
print('R:', r)
b = np.dot(q, r)
print('QR:', b)
a = np.array([[0, 2], 
              [2, 3]])
p = [1, 5, 10, 20]
for i in range(20):
    q, r = qr(a)
    a = np.dot(r, q)
    if i+1 in p:
        print(f'Iteration {i+1}:')
        print(a)
#%%
import numpy as np
def normalize(x):
    fac = abs(x).max()
    x_n = x / x.max()
    return fac, x_n 
x = np.array([1, 1, 1])
a=[[2,1,2],[1,3,2],[2,4,1]]
for i in range(8):
    x = np.dot(a, x)
    lambda_1, x = normalize(x)
    print("Eigenvalue:", lambda_1)
    print("Eigenvector:", x)
#%%
