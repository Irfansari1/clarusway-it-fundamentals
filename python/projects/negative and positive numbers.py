# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 20:44:48 2021

@author: admin
"""

# Write a Python program to rearrange positive and negative numbers in a given array using Lambda. 
#Sample Output:
#Original arrays:
#[-1, 2, -3, 5, 7, 8, 9, -10]
#Rearrange positive and negative numbers of the said array:
#[2, 5, 7, 8, 9, -10, -3, -1]


original = [-1, 2, -3, 5, 7, 8, 9, -10]
reversed_list = original[::-1]


neg = filter(lambda x : x<0, reversed_list)
pos = filter(lambda x : x>0, original)

print(list(pos)+list(neg))

original = [-1, 2, -3, 5, 7, 8, 9, -10]

re1 = []
re2 = []


for i in original:
    if i > 0 :
        re1.insert(0,i)
        re1.sort()
        
    elif i < 0 :
        re2.append(i)
        re2.sort()
        
print(re1+re2)

original = [-1, 2, -3, 5, 7, 8, 9, -10]

re1=list(filter(lambda x: x>0,original))
re1.sort()
print( re1)
re2 = list(filter(lambda x: x<0,original))
re2.sort()
print(re2)
print(re1+re2) #re1.extend(re2)