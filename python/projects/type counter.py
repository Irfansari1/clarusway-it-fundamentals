# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 19:28:47 2021

@author: admin
"""

data = ["a", "b", True, (False, 1), {"1" : 2}, [1,2], {"2" : "two"}, {2, "3"}, "c", 23, 0]
types = ["int", "str", "bool", "list", "tuple", "dict", "set"]
{}.fromkeys(types,0)
total = {}.fromkeys(types,0)
print(total)

print(len(data))

print(type(data[0]))

for i in range(len(data)):
    if type(data[i])==int : total["int"] +=1
    elif type(data[i])==str : total["str"] +=1
    elif type(data[i])==bool : total["bool"] +=1
    elif type(data[i])==list : total["list"] +=1
    elif type(data[i])==tuple : total["tuple"] +=1
    elif type(data[i])==dict : total["dict"] +=1
    elif type(data[i])==set : total["set"] +=1

print(total)