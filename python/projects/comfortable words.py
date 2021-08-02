# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 02:53:03 2021

@author: admin
"""

def comfortable_word(x):
    left = ["q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"]
    y = set(x)
    le = 0
    ri = 0
    for i in y:
        if i in left:
            le += 1
        else:
            ri += 1
    if ri != 0 and le != 0:
        return True
    else:
        return False
print(comfortable_word("tester"))
print(comfortable_word("polly"))
print(comfortable_word("clarusway"))
