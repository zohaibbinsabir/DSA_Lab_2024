# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 13:01:15 2024

@author: Code
"""

print()
print("Numpy Creating Arrays")
print()

#Import Numpy
import numpy as np

#Creating an ndarray
#We can create a array by passing a lsit, array and a tuple
arr = np.array([1,2,3,4,5])     #By passing a Array
print("1D Array By passing array :",arr)
print("Array Type :",type(arr))
print("Type of Array Values :",type(arr[0]))
print()

arr2 = np.array(("ali",'asif','shakir'))    #By passing a tuple
print("1D Array by passing Tuple :",arr2)
print("Type of array values :",type(arr2[0]))
print()

print("0D Array")
arr3 = np.array(24)
print("Type of Array :",arr3.ndim)
print("Array :",arr3)
print()

print("1D Array")
arr4 = np.array([1,2,3,4,5])
print("Type of Array :",arr4.ndim)
print("Array :",arr4)
print()

print("2D Array")
arr5 = np.array([[1,2],[3,4]])
print("Type of Array :",arr5.ndim)
print("Array :",arr5)
print()

print("3D Array")
arr6 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("Type of Array :",arr6.ndim)
print("Array :",arr6)
print()

print("Array having Higher Dimensions")
arr7 = np.array([1,2,3,4], ndmin=5)
print("Type of Array :",arr7.ndim)
print("Array :",arr7)
print()
