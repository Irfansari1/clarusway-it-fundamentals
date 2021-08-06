# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 22:04:33 2021

@author: admin
"""

girdi = input("Please enter an Asterix : ")
boyut = int(input("Please enter the dimension : "))
count = 0

while count < boyut:
    if count < boyut//2:
        print(((girdi + " ") *boyut)+"|")
    elif count == boyut//2:
        print((((girdi + " ") *boyut)+"|"),boyut, "x", boyut)
    else:
        print(((girdi + " ") *boyut)+"|")
    count +=1