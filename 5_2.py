# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 22:59:00 2023

@author: jaisi
"""

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n=int(num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest=n
    elif largest<n:
        largest=n
    if smallest is None:
        smallest=n
    elif smallest>n:
        smallest=n
print("Maximum is", largest)
print("Minimum is", smallest)
