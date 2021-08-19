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