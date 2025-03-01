# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 17:44:03 2023

@author: KIIT
"""

def isSorted(arr):
    n=len(arr)
    if n==0 or n==1:
        return True
    
    if arr[0]>arr[1]:
        return False
    
    else:
        return isSorted(arr[1:])
    
    


inp=[1,2,3,4,5,6]
print(isSorted(inp))