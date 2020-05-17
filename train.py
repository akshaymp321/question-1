#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:23:32 2020

@author: akshay
"""

seat_order = ['LOWER(1)','MIDDLE(2)','UPPER(3)','LOWER(4)','MIDDLE(5)','UPPER(6)','SIDE_LOWER(7)','SIDE_UPPER(8)']
Number=int(input () )-1
print(seat_order[(Number%8)])