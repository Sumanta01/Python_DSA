# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 22:09:20 2023

@author: KIIT
"""

def findLargestDigit(n):
    temp_str=str(n)
    largeDigit=int(temp_str[0])
    
    for i in temp_str[1:]:
        digit=int(i)
        if digit>largeDigit:
            largeDigit=digit
            
    return largeDigit



n=int(input())
print(findLargestDigit(n))