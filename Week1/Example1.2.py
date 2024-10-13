# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:17:38 2024

@author: Code
"""

print()
print("Input value from User")
print()

#input is always in string format
a = input("Enter a number: ")

#Type Casting
b = int(a)

#Convert int --> string in print() if using '+' in the place of ','
print("Your Entered Value is",b)
print("Your Entered Value is " + str(b))