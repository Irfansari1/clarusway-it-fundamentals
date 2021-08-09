# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 21:04:11 2021

@author: admin
"""

boyut = int(input("Please enter an odd number : "))
yapi = "*"
bosluk = " "
count = 0

while boyut %2==0:
    print("This is not an odd number")
    boyut = int(input("Please enter an odd number : "))
for i in range(1,boyut+1,2):
    print(int((boyut-i)/2)*bosluk, i*yapi, int((boyut-i)/2)*bosluk, "|")