'''
Created on 27-Jul-2022

@author: Rishi
'''
# convert list to ndarray 
import numpy as np 
from numpy import dtype

x = [1,2,3] 
a = np.asarray(x) 
print(a)

x = (1,2,3) 
a = np.asarray(x, dtype=float) 
print(a)
print("Individual Elements - if collections are also converted to Numpy ")
x = [(1,2,3),(4,5,6)] 
a = np.asarray(x)
print(a)

