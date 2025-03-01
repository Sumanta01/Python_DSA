# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:30:22 2023

@author: KIIT
"""

def findMaxDigit(n):
    if(n<0):
        return 0
    maxDigit=float('-inf')
    while(n>0):
        r=n%10;
        maxDigit=max(maxDigit,r)
        n//=10
        
    return maxDigit


n=int(input())
print(findMaxDigit(n))
    
    