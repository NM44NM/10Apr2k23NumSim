# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 13:06:30 2023

@author: 91703_0zbjuu
"""

def my_tip_calc(bill, party):
    if(party <6):
        tips=0.15*bill
    elif 6 <= party <8:
        tips=0.18*bill
    elif 8<= party <11:
            tips=0.20*bill
    else:
        tips=0.25*bill
    print (tips)
#%%
import numpy as np
def my_mult_operation(a, b, operation):
    out=0
    if operation== "plus":
        out =np.add(a,b)
    elif operation== "minus":
        out = np.subtract( a,b)
    elif operation == "div":
        out= np.divide (a,b)
    elif operation == "mult":
        out = np.multiply(a,b)
    elif operation == "pow":
        out=np.power(a,b)
    print(out)
#%%
    def area(x1,y1,x2,y2,x3,y3):
        return abs((x1*(y2-y3) +(x2*(y3-y1)) +(x3*(y1-y2)))/2)
def my_inside_triangle(x,y):
    position = ""
A= area(0,0,1,0,0,1)
A1= area(0,0,1,0,x,y)
A2= area(0,0,0,1,x,y)
A3= area(0,1,1,0,x,y)
if A1+A2+A3 == A:
    if A1==0 or A2==0 or A3==0:
        position ="Border"
    else:
        position ="Inside"
    else:
        position ="Outside"
        return position
#%%
def my_split_function():    
    if x<=a:
        return f(x)
    elif x>=b:
        return g(x)
    else:
        return 0
#%%
x = [7, 9, 10, 5, 8, 3, 4, 6, 2, 1]

def my_n_max(x, n):
    return out
#%%
