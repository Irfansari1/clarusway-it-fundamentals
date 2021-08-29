# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 22:18:43 2021

@author: admin
"""

#"Write a Python code that displays the unique vowels found in a word entered by the user."

#   "# List all the vowels\n",
vowels = ['a', 'e', 'i', 'o', 'u']

string = input("Please enter a string : ")

found = []
for letter in string:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)