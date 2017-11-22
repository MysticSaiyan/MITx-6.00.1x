#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:45:56 2017

@author: pragun
"""

num = 11

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False

result = ''

if num == 0:
    result = '0'

while num > 0:
    result = str(num%2) + result
    num = num//2
if isNeg:
    result = '-' + result

print(result)
    