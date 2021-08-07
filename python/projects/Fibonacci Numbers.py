# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 17:35:24 2021

@author: admin
"""

fib = [0,1]

for i in range (55):
    a = fib[i] + fib [i+1]
    fib.append(a)
    
    if a >50:
        break
    
print(fib)