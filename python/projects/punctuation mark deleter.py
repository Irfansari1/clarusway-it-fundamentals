# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:55:38 2021

@author: admin
"""

word=input("write anything :  ")
newword=""
for i in word:
    if i.isalnum():
        newword+=i
print(newword)