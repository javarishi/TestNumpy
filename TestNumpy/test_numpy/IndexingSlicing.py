'''
Created on 27-Jul-2022

@author: Rishi
'''
import numpy as np 
a = np.arange(10) 
print(a)
s = slice(2,7,2) 
print(a[s])
b = a[2:7:2] 
print(b)

print("a[2:] :: ", a[2:])
print("a[:4] :: ",a[:4])
print("a[-1] :: ",a[-1])

print(np.rand.random(10))
