# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 23:25:30 2021

@author: admin
"""
# take the first letters of a given integer and build an acronmy

name="North Way House"
name=name.split()
a=""
for i in name:
    a+="".join(i[0]).capitalize()
print(a)