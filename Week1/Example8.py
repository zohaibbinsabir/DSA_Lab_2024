# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:50:23 2024

@author: Code
"""

givenFile = open(file="Example8.txt", mode='r')
lines = givenFile.read()
arr = lines.split()
numbers = []
for i in arr:
    num = int(i)
    numbers.append(num)
    
print(numbers)