# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:30:52 2024

@author: Code
"""

print()
print("Slicing Arrays")
print()

import numpy as np

arr = np.array((1,2,3,4,5))
print("Slice Elements from index 1 to index 4 :", arr[1:5])
print("Slice Elements from index 4 to End :", arr[4:])
print("Slice Elements from Beginning to index 4 (not included) :",arr[:4])
print("Slicing using Negative Indexing :",arr[-3:-1])
print("Print Elemtns from index 1 to index 4 having 2 steps each :",arr[1:5:2])
print("Return Every other element from the array :",arr[::2])
print(arr.dtype)
print(arr.ndim)
print(type(arr))
print()

arr2 = np.array(((1,2,3,4,5),(6,7,8,9,10)))
print("From the Second Element, Slice Elemetns form index 1 to index 3 :",arr2[1,1:4])
print("From both Elements, Return index 2 :" ,arr2[0:,2])
print("From both elements, slice index 1 to index 3 :",arr2[0:,1:4])