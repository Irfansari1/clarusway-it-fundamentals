# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 22:28:50 2021

@author: admin
"""

def take_square(num1, num2):
    dictionary = dict()
    
    for i in range(num1, num2+1):
        if i % 2 != 0:
            dictionary[i] = i ** 2
            
    return dictionary

take_square(1, 20)