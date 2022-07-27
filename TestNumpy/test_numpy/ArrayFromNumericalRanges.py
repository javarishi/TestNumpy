'''
Created on 27-Jul-2022

@author: Rishi
'''
import numpy as np 
from numpy import dtype
print("range with step of 2")
x = np.arange(10,20,2) 
print(x)
print("5 Numbers from start to end")
x = np.linspace(10,20,4, endpoint = False)
# Note - linspace will always give float as output as its a division
print(x)
