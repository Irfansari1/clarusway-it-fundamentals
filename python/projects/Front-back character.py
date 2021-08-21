# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 13:30:25 2021

@author: admin
"""

def front_back(word):
    if len(word)<=1:
        return(word)
    else:
        return word[-1]+ word[1:-1]+word[0]

print(front_back('clarusway'))
print(front_back('a'))
print(front_back('ab'))