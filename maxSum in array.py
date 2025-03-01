# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 01:04:34 2024

@author: KIIT
"""

def maxSum(arr):
    large=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if i!=j:
                max_sum=arr[i]+arr[j]
                if max_sum>large:
                    large=max_sum
                    
            
    return large


ar=[1,2,3,4,5,6]
print(maxSum(ar))