# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 13:55:11 2021

@author: admin
"""
#perfect nummer example  --  6 = 1+2+3
num = 56
ls = []
#ls = [i for i in range(1,num) if num%i == 0 ]
for i in range(1,num):
    if num%i == 0:
        ls.append(i)
         
x = sum(ls)     
if x == num:
    print("Perfect")
else:
    print("not")
        
 