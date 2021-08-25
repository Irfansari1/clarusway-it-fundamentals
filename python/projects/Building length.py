# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 23:30:34 2021

@author: admin
"""

#get two points in  co-ordinate system from user
#get building length
#create code that calculate the distance between these two point.
#return a result, how mnay building can u build on line with 1 unit distance
#input  point 1 = 3,0  point 2 = 0,4 building length = 2
#output  line is 5 unit. And you can buil 2 times(with 2 unit lenght)

  
x_1 = int(input("X1 degerini girin"))
y_1 = int(input("y1 degerini girin"))
x_2 = int(input("x2 degerini girin"))
y_2 = int(input("y2 degerini girin"))

b_l = int(input("Building Length: "))

def built():
    result = 0
    c = 0
    length = ((x_1-x_2)*2+(y_1-y_2)*2)*0.5
    while True:
        result= result + b_l+1
        if result > length:
            break
        c += 1
    return c
        
    
     

print(built())