# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 23:25:13 2023

@author: jaisi
"""

score = input("Enter Score: ")
try:
    s=float(score)
except:
    print("Invalid input")
    quit()
if s>=0.9:
    print("A")
elif s>=0.8:
    print("B")
elif s>=0.7:
    print("C")
elif s>=0.6:
    print("D")
elif s<0.6:
    print("F")
