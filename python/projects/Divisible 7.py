# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 13:55:38 2021

@author: admin
"""
# kullanicidan liste al ve bu listede 7 ye bölünen elemanlari döndür
length = int(input("Enter the length of the list: "))
count = 1
ls = []
while count <= length:
    el = int(input(f"Give me the {count}. element: "))
    ls.append(el)
    count +=1
    
#for i in range( length ):
    #el = int(input(f"Give me the {i}. element: "))
   # ls.append(el)
    
print(ls)
#ls1=[]
#for i in ls:
   # if i%7 == 0:
       # ls1.append(i)
ls1=[]      
a = filter(lambda x:x%7 == 0, ls)
b = map(lambda y : y**2, ls)
        
print(list(a))
print(list(b))
        