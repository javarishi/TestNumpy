'''
Created on 26-Jul-2022

@author: Rishi
'''
import numpy as np

a = np.array([1,2,3,4])
print(a)
a = np.array([[1,2], [3,4]])
print(a)
a = np.array([[[1,2],[4,5]], [[6,7], [8,9]]])
print(a)
print("minimum dimensions") 
a = np.array([1,2,3,4,5,6], ndmin = 2) 
print(a)
print("dtype parameter")
a = np.array([1, 2, 3], dtype = complex) 
print(a)
print("8 bit int - i1 --> int16")
dt = np.dtype('i2')
a = np.array([10000,20000,30000,40000,50000], dt)
print(a)