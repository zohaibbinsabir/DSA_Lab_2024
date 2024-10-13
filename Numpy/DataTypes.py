# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:59:45 2024

@author: Code
"""

print()
print("Data Types")
print()

import numpy as np

print("Checking the datatype of an array")
arr = np.array([1,2,3,4,5])
print(arr.dtype)
print()

print("Creating arrays with a defined data type")
arr2 = np.array([1,2,3,4],'S')
print(arr2)
print(arr2.dtype)
print()

arr3 = np.array([1,2,3,4,5],dtype='i4')     # 4bytes integer
print(arr3)
print(arr3.dtype)
print()

print("Converting Data Type on Existing Arrays")
arr = np.array([1.1,1.2,1.3,1.4,1.5])
print(arr.dtype)
newArr = arr.astype('i')        #astype(int) is also true
print(newArr.dtype)