# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 13:29:41 2023

@author: KIIT
"""

def reverse(st):
    stack=[]
    rev=""
    for i in st:
        stack.append(i)
        
    while(stack):
        rev+=stack.pop()
        
    return rev
    


st="Habibi comes to KIIT"
print(reverse(st))
    
            