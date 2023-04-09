# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 09:14:06 2023

@author: 91703_0zbjuu
"""

y = 0
for i in range(1000):
    for j in range(1000):
        if i == j:
            y += 1
    print (j)
print(i)
#%%
def my_max(x):
    max=0
    for i in x:
        if max<i:
            max=i
    return max
#%%
def my_n_max(x,n):
    out=[]*n
    x=[7,8,9]
    for i in range(n):
        current_max=max(x)
        out.append(current_max)
        x.remove(current_max)
    return out
#%%
import math
def my_trig_odd_even(m):
    print("Input list-->",m)
    q=m
    for i in range(len(m)):
        for j in range(len(m[0])):
            if (m[i][j]%2)==1:
                q[i][j]= round(math.sin(m[i][j]),2)
            else:
                q[i][j]=round(math.cos(m[i][j]),2)
    return q
#%%
import numpy as np
def my_mat_mul(P,Q):
    P=np.array([[1,2,3,4],[5,6,7,8]])
    Q=np.array([[1,1,1],[2,2,2],[3,3,3],[4,4,4]])
    print('inputs list1", P')
    print('inputs list2", Q')
    P_rows=len(P)
    P_cols=len(P[0])
    Q_rows=len(Q)
    Q_cols=len(Q[0])
    M=[[0]*Q_cols]*P_rows
    if P_cols!=Q_rows:
        print('nope')
        return
    for i in range(0,P_rows):
        for j in range(0,Q_cols):
            M[i][j]=0
            for k in range(0, P_cols):
                M[i][j]=M[i][j]+P[i][j]+Q[i][j]
    return M
#%%
def my_savings_plan(PO,i,goal):
    years=0
    while PO<goal:
        PO=(1+i)*PO
        years+=1
    return years 
#%%
def my_fiind(M):
    i=[]
    for j in range(len(M)):
        if M[j]==1:
            i.append(j)
    return i
#%%
import random
def my_monopoly_dice():
    total=0
    flag=True
    while flag:
        a=random.randrange(1,6)
        b=random.randrange(1,6)
        print('dice nos',a,b)
        toal=total+a+b
        if a!=b:
            flag=False
    return total
#%%
def myisprime(n):
    for i in range(2,n-1,1):
        if n%i==0:
            return 0
    return 1
#%%
