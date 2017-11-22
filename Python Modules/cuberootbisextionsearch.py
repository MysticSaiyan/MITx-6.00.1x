#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:22:56 2017

@author: pragun
"""

cube = 12
epsilon = 0.01
num_guesses = 0
low = 1.0
high = cube
guess = (high+low)/2

while abs(guess**3 - cube) >= epsilon:
    print("High: " + str(high) + "| Low: " + str(low) + "| Guess: " + str(guess))
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high+low)/2
    num_guesses += 1
print("number of guesses : " , num_guesses)
print(guess," is close to the cube root of ",cube)