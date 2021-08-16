# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 14:04:12 2021

@author: admin
"""
#https://edabit.com/challenge/SHdu4GwBQehhDm4xT
ls = [1, 1, 0, 0, 0, 1]
count = 0
if ls[0] == 0:
    print("Not")
else: 

    for i in range(len(ls)):
        if ls[i] == 1:
            ls[i] = 0
        else:
            ls[i]  = 1
    
    for x in range(len(ls)):
        for j in range(len(ls)):
            if ls[j] == 1:
                ls[j]=0
            else:
                ls[j]  = 1
            
        print(ls)
        for y in range(len(ls)):
            if ls[y] == 1:
                count += 1
                ls = ls[y:]
                break
        if sum(ls) == 0:
            break
     
print(count)
    