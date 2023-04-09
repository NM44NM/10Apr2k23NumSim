# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 00:03:45 2023

@author: 91703_0zbjuu
"""

def my_bin_2_dec(b):
    d=0
    for digit in b:
        d=d*2 +int(digit)
        return d;
#%%
def my_dec_2_bin(d):
    b=[]
    if d==0: 
        b.append(0)
    while d>= 1:
            b.append(d%2)
            d= d//2
    b.reverse()
    return b;
#%%
def my_dec_2_bin(d):
    b=[]
    if d==0:
        b.append(0)
        while d>= 1:
            b.append(d%2)
            d= d//2
            b.reverse()
            return b;

def my_bin_2_dec(b):
    d=0
    for digit in b:
        d=d*2 +int(digit)
        return d;
#%%
def my_bin_adder (b1, b2):
    max_len=max(len(b1), len(b2))
    b1= [0]*(max_len- len(b1)) +b1
    b2= [0]*(max_len- len(b2)) +b2
    b=[]
    carry=0
    for i in range(max_len-1, -1, -1):
        sum= carry +b1[i] +b2[i]
        res=1 if sum%2 ==1 else 0
        b.append(res)
        carry= 0 if sum <2 else 1
    
    if carry != 0:
        b.append(1)
    
    b.reverse()
    return b