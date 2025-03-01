# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 17:51:14 2023

@author: KIIT
"""

def isSum(arr):
    n=len(arr)
    
    if not arr:
        return 0 

    return arr[0] + isSum(arr[1:])
    
    
inp=[21,5,12,32,1,43]
print(isSum(inp))