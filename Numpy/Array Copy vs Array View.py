# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:13:14 2024

@author: Code
"""

print()
print("Array Copy vs View")
print()

import numpy as np

arr = np.array([1,2,3,4,5])
x = arr.copy()
y = arr.view()

x[1] = 0
y[0] = 0

print(arr)
print(x)
print(y)

arr[0] = 1
print(arr)
print(y)

print(arr.base)
print(x.base)
print(y.base)