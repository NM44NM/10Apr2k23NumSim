# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 21:42:14 2023

@author: 91703_0zbjuu
"""

import numpy as np
def my_int_calc(f, f0, a, b,N, option):
    h = (b-a)/(N-1)
    x = np.linspace(a,b,N)
    F = f(x)
    def riemannIntegral(F, h):
        return h * sum(F[1::])
    def trapezoidRule(F, h):
        return (h / 2) * (F[0] + 2 * sum(F[1:N - 1]) + F[N - 1])
    def simpsonMethod(F, h):
        if (len(F)%2 == 0):
            raise BaseException("Error: Simpson method can work only with odd number of data points!")
            return
        return (h / 3) * (F[0] + 2 * sum(F[:N - 2:2]) + 4 * sum(F[1:N - 1:2]) + F[N - 1])
    I = 0
    if (option == "trap"):
        I = trapezoidRule (F, h)
    elif (option == "rect"):
        I = riemannIntegral(F, h);
    elif (option == "simp"):
        I = simpsonMethod(F, h);
    else:
        print("Invalid option!")
        return;
    I = I + f0
    return I
def f(x):
    return np.sin(x)
I = my_int_calc(f, 0, 0, 3, 99, 'rect')
print("Riemann", I)
I = my_int_calc(f, 0, 0, 3, 99, 'trap')
print("Trapezoidal", I)
I = my_int_calc(f, 0, 0, 3, 99, 'simp')