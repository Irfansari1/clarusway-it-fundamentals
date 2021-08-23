# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:15:10 2021

@author: admin
"""
from collections import Counter

sentence = input("Please enter a sentence: ")
str_1 = list(sentence)
cnt = Counter()

for letter in str_1:
    cnt[letter] += 1

cnt = dict(cnt)
print(cnt)


"""
str_1 = "hippopotamus"
dict_1 ={}

for i in str_1:
    a=str_1.count(i)
    dict_1[i] = a
    print(a)
print(dict_1)
"""