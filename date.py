#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:31:10 2020

@author: akshay
"""

day=int(input("enter day:"))
month=int(input("enter month:"))
year=int(input("enter year:"))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    maximum_days=31
elif month==4 or month==6 or month==9 or month==11:
    maximum_days=30
elif year%4==0 and year%100==0 or year%400==0:
    maximum_days=29
else:
    maximum_days=28
if month<1 or month>12:
    print("entered date is invalid:")
    print("check the range of month:")
elif day<1 or day>31:
    print("entered day is invalid:")
    print("check the range of day:")
elif year<0 or year>2020:
    print("entered year is invalid:" )
else:
    print ("entered date is valid:")
    

    