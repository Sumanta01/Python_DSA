# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:08:12 2024

@author: KIIT
"""


def factorial(n):
    if n<2:
        return 1
    
    return n*factorial(n-1)

def strongNumber(n):
    temp=n
    sum_fact=0
    while n>0:
        digit=n%10
        sum_fact+=factorial(digit)
        n//=10
        
    return sum_fact==temp


num=int(input())
print(strongNumber(num))


