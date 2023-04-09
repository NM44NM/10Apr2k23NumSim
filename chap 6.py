# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 20:19:54 2023

@author: 91703_0zbjuu
"""

def factorial(n):
       if n == 1:
        return 1 
       else:
        return n*factorial(n - 1)   
#%%
def fibonacci(n):
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
#%%
import numpy as np

def iterafib(n):
    fib = np.ones(n)
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib
#%%
def my_towers(N, from_tower, to_tower, alt_tower):
    if N != 0:
        my_towers(N-1, from_tower, alt_tower, to_tower)
        print("Move disk %d from tower %d to tower %d." %(N, from_tower, to_tower))
        my_towers(N-1, alt_tower, to_tower, from_tower)
#%%
def my_quicksort(lst):
    if len(lst) <= 1:
       sorted_list = lst    
    else:
        pivot = lst[0]
        bigger = []
        smaller = []
        same = []
        for item in lst:
            if item > pivot:
                bigger.append(item)
            elif item < pivot:
                smaller.append(item)
            else:
                same.append(item)
        sorted_list = my_quicksort(smaller) + same + my_quicksort(bigger)
        return sorted_list
#%% 
import numpy
def my_sum(lst):
    arr=numpy.array(lst)
    if arr.size==1:
        return arr[0]
    else:
        current= arr[arr.size-1]
        arr=numpy.resize(arr,arr.size-1) 
    return current + my_sum(arr)
#%%
def my_chebyshev_polyl(n,x):
    m=len(x)
    y=[]*m
    for i in range (0, m):
        y.append(chebyshev(n, x[i]))
        return y
        def chebyshev(n, elem):
            if n == 0:
                return 1
            elif n == 1:
                return elem
            else:
                elem=2*elem*chebyshev(n-1,elem)-chebyshev(n-2,elem)
            return elem
#%%
def my_ackermann(m, n):
    if m == 0:
        return n+1 
    if m>0 and n ==0:
        return my_ackermann(m-1, 1)
    if m>0 and n>0:
        return my_ackermann(m-1, my_ackermann(m, n-1))
    else:
        print("INVALID values of m or n.")
#%%
def my_n_choose_k(n, k):
    if n==k:
        return 1
    if k==1:
        return n
    return my_n_choose_k(n-1, k) + my_n_choose_k(n-1, k-1)
#%%
def my_change(cost, paid):
    amount=paid-cost
out=[]
make_change(amount, out)
return out
#%%
def make_change(amt, lis):
    denominations=[100,50,20,10,5,1, .5, .25, .1, .05, .01]
    i=0
    if amt > 0.009:
        while denominations[i] > amt:
            i+=1
    amt -= denominations[i]
    lis.append(denominations[i])
    else
        return lis
    return make_change(amt,lis)
#%%
def my_gcd(a, b):
    if b==0:
        gcd = a
    else:
        gcd = my_gcd(b, a % b)
    return gcd
print(my_gcd(10, 4))
print(my_gcd(33, 121))
print(my_gcd(18, 1))
#%%
def my_pascal_row(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        row = [1]
        last_row = my_pascal_row(n-1)
        for i in range(1,len(last_row)):
            row.append(last_row[i-1] + last_row[i])
            row += [1]
        return row
#%%
def my_spiral_ones(n):
    if ( n == 0 ):
        print(" Invalid input 0 , try again .. ")
        Exit(0)
    if ( n == 1 ):
        return [1]
    tempA = my_spiral_ones(n-1)
    if ( n == 2 ):
        tempA = [ tempA ]
        sumBottom = 0
        sumTop = -1
    elif ( n == 3 ):
        sumBottom = -1
        sumTop = -1
        else :
            sumTop = sum ( tempA[0] )
            sumBottom = sum ( tempA[-1] )
            resultA = None
            if ( sumBottom == n-2 ) :
                resultA = tempA + [[0 for x in range (n-1) ]]
#%%
