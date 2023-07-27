# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 13:29:00 2023

@author: jaisi
"""

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r=float(rate)
if h<=40:
    pay=h*r
    print(pay)
elif h>40:
    pay=(40*r)+((h-40)*1.5*r)
    print(pay)
