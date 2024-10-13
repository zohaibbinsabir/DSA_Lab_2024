# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 08:39:38 2024

@author: Code
"""

import random as rd

print()
print("Printing Random Array of size 5 in range of 0 - 50")
arr = []
min = 0
max = 50
n = 5

for i in range(5):
    num = rd.randint(min, max)
    arr.append(num)
    
print(arr)
print()

print("Same using Numpy")
import numpy as np
arr2 = []
for i in range(n):
    num = np.random.randint(min,max)
    arr2.append(num)

print(arr2)