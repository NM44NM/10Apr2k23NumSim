# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 00:58:58 2023

@author: 91703_0zbjuu
"""
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')
x = np.linspace(0, 1, 101)
y = 1 + x + x * np.random.random(len(x))
A = np.vstack([x, np.ones(len(x))]).T
y = y[:, np.newaxis]
alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),y)
print(alpha)
plt.figure(figsize = (10,8))
plt.plot(x, y, 'b.')
plt.plot(x, alpha[0]*x + alpha[1], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
pinv = np.linalg.pinv(A)
alpha = pinv.dot(y)
print(alpha)
alpha = np.linalg.lstsq(A, y, rcond=None)[0]
print(alpha)
x = np.linspace(0, 1, 101)
y = 1 + x + x * np.random.random(len(x))
def func(x, a, b):
    y = a*x + b
    return y
alpha = optimize.curve_fit(func, xdata = x, ydata = y)[0]
print(alpha)
#%%
import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([0,0.8,0.9,0.1,-0.6,-0.8,-1,-0.9,-0.4,2])
A=np.vstack([x,np.ones(len(x))]).T
plt.figure(figsize=(24,10))
i=2
plt.subplot(2,3,i)
plt.plot(x,y,"o")
plt.plot(x,y_est[0]*x**2+y_est[1]*x+0,"r",label="multivariant regression")
plt.title(f"Polynomial of order{i}Least square regression formula")
plt.legend()
plt.tight_layout()
plt.show()