#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 17:09:00 2020

@author: akshay
"""

n=int(input("enter the number:"))
t=n
r=0
while(n>0):
 a=n%10
 r=r+a*a*a
 n=n//10
if(r==t) :
      print ("amstrong number:")
else:
     print ("not a amstrong number:")
