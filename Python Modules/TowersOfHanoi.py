#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:32:40 2017

@author: pragun
"""

def printMove(A='A', B='B'):
    print('move from ' + str(A) + ' to ' + str(B))

def Towers(n, A='A', B='B', spare='S'):
    global move             #so funtion can rewrite it
    if n == 1:
        printMove(A, B)
        move += 1

    else:
        Towers(n-1, A, spare, B)
        Towers(1, A, B, spare)
        Towers(n-1, spare, B, A)

move = 0
Towers(10)
print('it will take:', move, 'moves')