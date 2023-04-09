# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 20:55:17 2023

@author: 91703_0zbjuu
"""

class People():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        def greet(self):
            print("Greetings, " + self.name)
            person1 = People(name = 'Iron Man', age = 35)
            person1.greet()
            print(person1.name)
            print(person1.age)
#%%
class Student():
    def init(self, sid, name, gender):
        self.sid = sid
        self.name = name
        self.gender = gender
        self.type = 'learning'
        def say_name(self):
            print("My name is " + self.name)
#%%
import numpy as np
vector_row = np.array([[1, -5, 3, 2, 4]])
vector_column = np.array([[1], 
                          [2], 
                          [3], 
                          [4]])
print(vector_row.shape)
print(vector_column.shape)
#%%
from numpy.linalg import norm
new_vector = vector_row.T
print(new_vector)
norm_1 = norm(new_vector, 1)
norm_2 = norm(new_vector, 2)
norm_inf = norm(new_vector, np.inf)
print('L_1 is: %.1f'%norm_1)
print('L_2 is: %.1f'%norm_2)
print('L_inf is: %.1f'%norm_inf)
#%%
from numpy import arccos, dot

v = np.array([[10, 9, 3]])
w = np.array([[2, 5, 12]])
theta = \
    arccos(dot(v, w.T)/(norm(v)*norm(w)))
print(theta)
#%%
P = np.array([[1, 7], [2, 3], [5, 0]])
Q = np.array([[2, 6, 3, 1], [1, 2, 3, 4]])
print(P)
print(Q)
print(np.dot(P, Q))
np.dot(Q, P)
#%%
a = [[8, 3, -3], [-2, -8, 5], [3, 5, 10]]
diag = np.diag(np.abs(a)) 
off_diag = np.sum(np.abs(a), axis=1) - diag 
if np.all(diag > off_diag):
    print('matrix is diagonally dominant')
else:
    print('NOT diagonally dominant')


x1 = 0
x2 = 0
x3 = 0
epsilon = 0.01
converged = False

x_old = np.array([x1, x2, x3])

print('Iteration results')
print(' k,    x1,    x2,    x3 ')
for k in range(1, 50):
    x1 = (14-3*x2+3*x3)/8
    x2 = (5+2*x1-5*x3)/(-8)
    x3 = (-8-3*x1-5*x2)/(-5)
    x = np.array([x1, x2, x3])
    dx = np.sqrt(np.dot(x-x_old, x-x_old))    
    print("%d, %.4f, %.4f, %.4f"%(k, x1, x2, x3))
    if dx < epsilon:
        converged = True
        print('Converged!')
        break
    x_old = x

if not converged:
    print('Not converge, increase the # of iterations')
#%%
import numpy as np

A = np.array([[4, 3, -5], 
              [-2, -4, 5], 
              [8, 8, 0]])
y = np.array([2, 5, -3])

x = np.linalg.solve(A, y)
print(x)
A_inv = np.linalg.inv(A)
x = np.dot(A_inv, y)
print(x)
from scipy.linalg import lu

P, L, U = lu(A)
print('P:\n', P)
print('L:\n', L)
print('U:\n', U)
print('LU:\n',np.dot(L, U))
print(np.dot(P, A))
#%%
import numpy as np
def isidentical(prodwithA,sumofABAC):
    for i in range(len(prodwithA)):
        for j in range(len(sumofABAC)):
            if prodwithA[i][j] != sumofABAC[i][j]:
                return 0
            return 1
        A=np.array([[1,2,3],[2,3,4],[3,4,5]])
        B=np.array([[1,1,1],[2,2,2],[3,3,3]])
        C=np.array([[1,3,5],[3,5,7],[5,7,11]])
        sumofBC=B+C
        print ("B+C=",sumofBC)
        prodwithA=np.dot(A,sumofBC)
        print ("A.(B+C)= ",prodwithA)
        AB=np.dot(A,B)
        AC=np.dot(A,C)
        print ("A.B=",AB)
        print ("B.C=",AC)
        sumofABAC=AB+AC
        print ("AB+AC=",sumofABAC)
        if isidentical(prodwithA,sumofABAC)== 1:
            print("Commutative:A(B+C)=AB+AC")
        else :
            print("Non-Commutative")
#%%
import numpy as np
from numpy.linalg import norm
from numpy import arccos,dot,clip
def my_is_orthogonal(v1,v2,tol):
    vector1=v1.T/norm(v1)
    vector2=v2/norm(v2)
    dotprod=np.dot(vector1,vector2)
    theta=np.arccos(clip(dotprod,-1,1))
    print(theta)
    val=np.abs(np.pi/2-theta)
    if val >= tol:
        return 0
    return 1
a=np.array([[1],[0.001]])
b=np.array([[0.001],[1]])
print ("1.")
o1=my_is_orthogonal(a,b,0.01)
print ("output1=",o1)
print ("2")
o2=my_is_orthogonal(a,b,0.001)
print ("output2=",o2)
a=np.array([[1],[0.001]])
b=np.array([[1],[1]])
print ("3")
o3=my_is_orthogonal(a,b,0.001)
print ("output3=",o3)
print ("4")
a=np.array([[1],[1]])
b=np.array([[-1],[1]])
o4=my_is_orthogonal(a,b,1e-10)
print ("output4=",o4)
#%%
