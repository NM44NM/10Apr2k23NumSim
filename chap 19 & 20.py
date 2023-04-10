# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 08:32:45 2023

@author: 91703_0zbjuu
"""

import numpy as np
from scipy import optimize
f = lambda x: np.cos(x) - x
r = optimize.fsolve(f, -3)
print("r =", r)
result = f(r)
print("result=", result)
f = lambda x: 1/x
r, infodict, ier, mesg = optimize.fsolve(f, -3, full_output=True)
print("r =", r)
result = f(r)
print("result=", result)
print(mesg)
#%%
import numpy as np
def my_bisection(f, a, b, tol): 
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("no root")
    m = (a + b)/2
    if np.abs(f(m)) < tol:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection(f, m, b, tol)
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection(f, a, m, tol)
f = lambda x: x**2 - 2
r1 = my_bisection(f, 0, 2, 0.1)
print("r1 =", r1)
r01 = my_bisection(f, 0, 2, 0.01)
print("r01 =", r01)

print("f(r1) =", f(r1))
print("f(r01) =", f(r01))
my_bisection(f, 2, 4, 0.01)
#%%
import numpy as np

f = lambda x: x**2 - 2
f_prime = lambda x: 2*x
newton_raphson = 1.4 - (f(1.4))/(f_prime(1.4))

print("newton_raphson =", newton_raphson)
print("sqrt(2) =", np.sqrt(2))
def my_newton(f, df, x0, tol):
    if abs(f(x0)) < tol:
        return x0
    else:
        return my_newton(f, df, x0 - f(x0)/df(x0), tol)
estimate= my_newton(f, f_prime, 1.5, 1e-6)
print("estimate =", estimate)
print("sqrt(2) =", np.sqrt(2))
#%%
def my_nth_root(x, n, tol):
    f = lambda y: y**n - x
    _prime = lambda y: n*(y**(n-1))
    r = 1
    r = my_newton(f, f_prime, r, tol)
    return r
#%%
def my_fixed_points(f,g,tol,max_iter):
    F = lambda x : f(x) - g(x)
    def guess(f,initial):
        istart = initial - 1
        iend = initial + 1  
        limit = 10000000
        i = 1
        while i < limit:
            if ( f( istart) < 0 ) & ( f( iend) > 0 ):
                a = istart;
                b = iend;
                return [a, b]
            elif f(istart) > 0:
                istart = istart - 2*istart
            else:                
                iend = iend + 2*iend
            i+=1
    [a,b] = guess(F,0)
    i = 1
    def sign(a):
        return (a > 0) - (a < 0)
    while(i, max_iter):
        m = (a+b)/2
        if (abs(F(m)) < tol):
            return m
        elif (sign(F(m)) == sign(F(a))):
            a = m
        else:
            b = m
    return []
#%%
def myBisection(f, a, b, tol):
    n = np.ceil(np.log2((b-a)/tol))
    R = np.zeros(int(n))
    E = np.zeros(int(n))
    def sign(a):
        if (a == 0):
            return a
        return a/abs(a)
    limit = n
    i = 0
    while(i,limit):
          R[i] = (a+b)/2
          E[i] = abs(f(R[i]))
          if (E[i] < tol):
            R[np.isnan(R)] = []
            E[np.isnan(R)] = []
          elif (sign(f(R[i]))  == sign(f(a))):
            a = R[i]
          else:
            b = R[i]
            i += 1
    return [R, E]
#%%
import numpy as np
def myBisection(f, a, b, tol):
    n = np.ceil(np.log2((b-a)/tol))
    R = np.zeros(int(n))
    E = np.zeros(int(n))
    limit = n ;
    i = 0
    def sign(a):
        if (a == 0):
            return a
        return a/abs(a)
    while(i<limit):
        R[i] = (a+b)/2
        E[i] = abs(f(R[i]))
        if (E[i] < tol):
            R[np.isnan(R)] = []
            E[np.isnan(R)] = []
        elif (sign(f(R[i]))  == sign(f(a))):
            a = R[i]
        else:
            b = R[i]
        i += 1
    return [R, E]
f1 = lambda x:  x**2 - 2;
low = 0;
high = 2;
tolerance =   1e-1;
[R, E] = myBisection(f1, low, high, tolerance)
print([R, E])
f2 = lambda x:  np.sin(x) - np.cos(x);
tolerance = 1e-2;
[R, E] = myBisection(f2, low, high, tolerance)
print([R, E])
#%%
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')
h = 0.1
x = np.arange(0, 2*np.pi, h) 
y = np.cos(x) 
forward_diff = np.diff(y)/h 
x_diff = x[:-1:] 
exact_solution = -np.sin(x_diff) 
plt.figure(figsize = (12, 8))
plt.plot(x_diff, forward_diff, '--', \
         label = 'Finite difference approximation')
plt.plot(x_diff, exact_solution, \
         label = 'Exact solution')
plt.legend()
plt.show()
max_error = max(abs(exact_solution - forward_diff))
print(max_error)
#%%
import numpy as np
import math

h = 1
iterations = 20
step_size = [] 
max_error = [] 
for i in range(iterations):
    h /= 2 
    step_size.append(h) 
    x = np.arange(0, 2 * np.pi, h) 
    y = np.cos(x) 
    forward_diff = np.diff(y)/h 
    x_diff = x[:-1] 
    exact_solution = -np.sin(x_diff) 
    max_error.append(max(abs(exact_solution - forward_diff)))
plt.figure(figsize = (12, 8))
plt.loglog(step_size, max_error, 'v')
plt.show()
#%%
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')
x = np.arange(0, 2*np.pi, 0.01)
omega = 100
epsilon = 0.02
y = np.cos(x) 
y_noise = y + epsilon*np.sin(omega*x)
plt.figure(figsize = (12, 8))
plt.plot(x, y_noise, 'r-', label = 'cos(x) + noise')
plt.plot(x, y, 'b-', label = 'cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
