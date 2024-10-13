# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:35:42 2024

@author: Code
"""

print()
print("Array of Zeros")
print()

arr1 = [0] * 10
print("1D array of length = 10:",arr1)

arr3 = [[0 for x in range(4)] for y in range(3)]
print("2D array of Length(4*3) By Method2 :",arr3)

import numpy as np

arr4 = np.zeros(5,int)
print(arr4)

arr5 = np.zeros((2,3),int)
print(arr5)