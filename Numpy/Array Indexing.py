# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:16:15 2024

@author: Code
"""

print()
print("Numpy Array Indexing")
print()

#Import Numpy
import numpy as np

arr = np.array((1,2,3,4,5))
print("First Element of Array is : " + str(arr[0]))
print("Second Element of Array is : " + str(arr[1]))
print("Third Element of Array is :" , str(arr[2]))
print()

arr2 = np.array(((1,2,3,4,5),(6,7,8,9,10)))
print("2nd Element of first row :",arr2[0,1])
print("5th element of 2nd row :",arr2[1,4])
print()

arr3 = np.array((((1,2,3),(4,5,6)),((7,8,9),(10,11,12))))
print("Third Element of Second Array of the First Array :",arr3[0,1,2])
print()

print("Negative Indexing")
print()
print()

print("2nd Element of First Row :",arr2[-2,-4])