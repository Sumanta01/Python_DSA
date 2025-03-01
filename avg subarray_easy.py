# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 00:57:43 2024

@author: KIIT
"""

def sliding_window_principle(arr,k):
    cur_subarr=sum(arr[:k])
    res=[cur_subarr]
    
    for i in range(1,len(arr)-k+1):
        cur_subarr=cur_subarr-arr[i-1]
        cur_subarr=cur_subarr+arr[i+k-1]
    
        res.append(cur_subarr)
        
    return max(res)/k


arr=[1,12,-5,-6,50,3]
k=4
print(sliding_window_principle(arr, k))
        