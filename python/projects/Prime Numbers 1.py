# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 19:27:09 2021

@author: admin
"""

print("This program will check if your integer input is prime.")
num = int(input("Enter a integer number first: "))
ls =[]
 

if num < 2:
    print("The number can not be smaller than 2.")
elif num == 2:
    print(f"{num} is a prime nummber")
else:   
    for i in range(2,num):
        if (num % i) == 0:
            ls.append(i)
    if bool(ls) == True:      
            print(f"{num} is not a prime number.\n{num} has {len(ls)} divisors and those are below:\n{ls}")
    else:
        print(f"{num} is a prime nummber")