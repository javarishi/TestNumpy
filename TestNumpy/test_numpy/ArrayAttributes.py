'''
Created on 27-Jul-2022

@author: Rishi
'''
import numpy as np 
a = np.array([[1,2,3],[4,5,6]]) 
print(a.shape)
# a.shape = (3,2) 
b = a.reshape(3,2) 
print("Original")
print(a)
print("reshape")
print(b)
print("range function provided by Numpy")
a = np.arange(24) 
b = a.reshape(2,4,3) 
print(a)
print("reshape")
print(b)
print("itemsize : bytesize of data")
x = np.array([1,2,3,4,5], dtype = np.int8) 
print (x.itemsize)
