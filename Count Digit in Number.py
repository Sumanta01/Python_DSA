# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 00:11:32 2023

@author: KIIT
"""

def CountDigit(n):
    if n==0:
        return 0
    return  1 + CountDigit(n//10)

ip=int(input())
print(CountDigit(ip))