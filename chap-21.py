# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:42:32 2023

@author: 91703_0zbjuu
"""

import numpy as np
a=0
b=np.pi
n=22
h=(b-a)/(n-1)
x=np.linspace(a,b,n)
f=np.sin(x)
I_trap= (h/2)*(f[0]+ 2*sum(f[1:n-1]) +f[n-1])
err_trap= 2-I_trap
print(I_trap)
print(err_trap)
#%%
import numpy as np
a=0
b=np.pi
n=33
h=(b-a)/(n-1)
x=np.linspace(a,b,n)
f=np.sin(x)
I_simp= (h/3)*(f[0]+ 2*sum(f[:n-2:2])+4*sum(f[1:n-1:2])+f[n-1])
err_simp= 2-I_simp
print(I_simp)
print(err_simp)
#%%
import numpy as np
a=0
b=np.pi
n=44
h=(b-a)/(n-1)
x=np.linspace(a,b,n)
f=np.sin(x)

I_reimannL= h*sum(f[:n-1])
err_reimannL=2-I_reimannL
I_reimannR= h*sum(f[:n-1])
err_reimannR=2-I_reimannR
I_mid=h*sum(np.sin((x[:n-1] + x[:1])/2))
err_mid=2-I_mid

print(I_reimannL)
print(err_reimannL)

print(I_reimannR)
print(err_reimannR)

print(I_mid)
print(err_mid)