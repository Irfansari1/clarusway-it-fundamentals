# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 16:37:48 2021

@author: admin
"""
while True:
   try:
       num = int(input("Give me a number: "))
   except:
       print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")
       continue

a = str(num)
result = 0
for i in range(len(a)):
    result = result + int(a[i]) ** len(a)
if num == result:
    print(f"Correct! {num} is Armstrong Number.")
else:
    print(f"Sory! {num} is not an Armstrong Number.")