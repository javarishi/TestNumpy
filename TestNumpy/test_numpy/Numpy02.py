'''
Created on 26-Jul-2022

@author: Rishi
'''
import numpy as np
from numpy import dtype

# first create structured data type 
dt = np.dtype([('age', np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt) 
print(a)
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('David', 15, 50),('Niel', 14, 75)], dtype = student) 
print(a)