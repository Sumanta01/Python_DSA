# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 03:11:38 2023

@author: KIIT
"""

def reverse(Str):
    rev=""
    for i in range(len(Str)-1,-1,-1):
        rev+=Str[i]
        
    return rev
        
        

Str1=input()
print(reverse(Str1))
        