# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:32:41 2024

@author: Code
"""

print("Write array elements one per line to file")

arr = ['Hello World',"Master"]
f = open(file="Example9.txt", mode="w")
for i in arr:
    f.write(i + "\n")