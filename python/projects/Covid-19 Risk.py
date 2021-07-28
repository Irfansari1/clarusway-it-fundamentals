# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 10:45:57 2021

@author: admin
"""

age= bool(input("Are you a cigarette addict older than 75 years old?: "))
chronic= bool(input("Do you have a severe chronic disease?: "))
immune= bool(input("Is your immune system too weak?: "))

if age == True:
    print("You are in risky group")
    
elif chronic == True:
    print("You are in risky group")
    
elif immune == True:
    print("You are in risky group")
    
else: 
    print("You are not in risky group")