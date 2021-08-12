# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 00:24:52 2021

@author: admin
"""

n = list(range(1, 101))

for i in range(0, len(n)) :
    
    if n[i] %5==0 and  n[i] %3==0 :
        n[i] = "FizzBuzz"
        
    elif n[i] %5==0 :
        n[i] = "Buzz"
        
    elif  n[i] %3==0 :
        n[i] = "Fizz"
        
    else:
        n[i] = n[i]
              
print(n)




n = list(range(1, 101))
def a(n):
    
 
        
    if  n %5==0 and  n %3==0 :
            n  = "FizzBuzz"
            
    elif n  %5==0 :
            n = "Buzz"
            
    elif  n  %3==0 :
            n  = "Fizz"
            
    else:
            n  = n 
              
    return n   
    
 
 
print(list(map(a,n)))


ls = []
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        i = "FizzBuzz"
        ls.append(i)
    elif i%5 == 0:
        i = "Buzz"
        ls.append(i)
    elif i%3 == 0:
        i = "Fizz"
        ls.append(i)
    else:
        ls.append(i)
        
print(ls)