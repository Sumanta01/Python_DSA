# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:45:42 2023

@author: KIIT
"""

def countDigit(n,digit):
    count=0
    while(n>0):
        if n%10==digit:
            count+=1
        
        n//=10
    
    return count

inp_n=int(input())
inp_digit=int(input())
print(countDigit(inp_n, inp_digit))