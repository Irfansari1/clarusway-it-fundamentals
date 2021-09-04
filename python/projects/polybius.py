# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 19:00:26 2021

@author: admin
"""

#The Polybius Square cipher is a simple substitution cipher that makes use of a 5x5 square grid. The letters A-Z are written into the grid, with "I" and "J" typically sharing a slot (as there are 26 letters and only 25 slots).
from string import ascii_uppercase
 
ls_letters = list(ascii_uppercase)
ls = []
ls = [str(i)+str(j)for i in range(1,6) for j in range(1,6)]
    
ls_letters.remove("J")
i = ls_letters.index("I")
ls_letters[i] = "I/J"

dict_letter = dict(zip(ls,ls_letters)) # my dict which is consist of numbers as keys and values as letters(11:"A")
 

def polybius(inp):

    #if input consist of numbers
    if inp[0] not in ls_letters:
         
        a =""
        b = []# main list
        
        for y in inp:
            if y == " ":
                b.append(" ")
            else:
                a = a + y
                if len(a) == 2 :
                     b.append(a)
                     a = "" 
        out = ""
        for x in b:
            if x == " ":
                out = out +" "
            elif x == "24":
                out = out +"I"
            else:
                out = out + dict_letter[x]
        return out
        
     
    #if input consist of letters
    else:
        inp = inp.upper()
        
        reversed_dict =  {v: k for k, v in dict_letter.items()}
         
        out2 =""
        for n in inp:
            if n == " ":
                out2 = out2 + " "
            elif n == "I":
                out2=out2+"24"
            else:
                out2 = out2 + reversed_dict[n]
        return out2
        
    
print(polybius("2315313134 3254 33113215 2443 3455251133"))