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