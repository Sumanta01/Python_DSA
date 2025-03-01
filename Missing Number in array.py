# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 02:48:46 2023

@author: KIIT
"""

def missingNumber(arr,n):
    sum_N=n*(n+1)//2
    
    sum_A=sum(arr)
    
    return sum_N - sum_A



arr=[1,2,4,6,3,7,8]
n=(len(arr))+1
print(missingNumber(arr, n))