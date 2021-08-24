# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 23:33:24 2021

@author: admin
"""

#pascal triangle
n = int(input("n value? "))
st=" "
main = []
ls = [1]
ls1 = [1]
ls2 = [1,1]
main.append(ls1)
main.append(ls2)
for j in range(n-2):
    for i in range(len(ls2)-1):
        result = ls2[i]+ls2[i+1]
        ls.append(result)
       
    
    ls.append(1)
    main.append(ls)
    ls2=ls
    ls = [1]
    
 

for x in range(1,n+1):
    print((n-x)*st,main[x-1])