# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:17:55 2024

@author: Code
"""

print()
print("Array Shape")
print()

import numpy as np

arr = np.array([1,2,3,4,5])
print(arr.shape)

arr2 = np.array([[1,2],[3,4]])
print(arr2.shape)

arr3 = np.array([1,2,3,4,5],ndmin=5)
print(arr3.shape)