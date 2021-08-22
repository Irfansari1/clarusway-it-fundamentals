# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:49:21 2021

@author: admin
"""

"""  
def front_back(word):
    return word.replace(word[0], word[-1])
    return word.replace(word[-1], word[0])
print(front_back('kitchen'))
 """
def front_back(word):
    if len(word)<=1:
        return(word)
    else:
        return word[-1]+ word[1:-1]+word[0]

print(front_back('clarusway'))
print(front_back('a'))
print(front_back('ab'))