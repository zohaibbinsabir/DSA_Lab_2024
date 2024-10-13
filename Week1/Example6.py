# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 08:50:38 2024

@author: Code
"""

print("Traverse in forward direction using for loop")
str = ["a","b","c"]
for x in range(len(str)):
    print(str[x])
    
print()
print("Reverse by using a slice")
print(str[::-1])
print()

print("Traverse in backward direction using reverse method")
str.reverse()
print(str)
print()

print("Traverse through an array using for loop")
for i in range(len(str)-1,-1,-1):
    print(str[i])