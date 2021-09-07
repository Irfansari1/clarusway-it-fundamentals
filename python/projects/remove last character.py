# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 23:16:25 2021

@author: admin
"""

"""Remove last character in list of strings:
 given_list = ["Lessons", "Words", "Pythons", "Programers","Clarusways"] 
 expected output : ['Lesson', 'Word', 'Python', 'Programer', 'Clarusway']
 """

given_list = ["Lessons", "Words", "Pythons", "Programers","Clarusways"]
 
print(list(map(lambda x: x.replace(x[len(x)-1],""),given_list)))