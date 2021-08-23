# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:49:21 2021

@author: admin
"""


def missing_char(word, n):
    return word.replace(word[n], "")

print(missing_char('kitchen', 1))
