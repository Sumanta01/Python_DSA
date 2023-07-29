# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 02:13:15 2023

@author: KIIT
"""

def findans(arr):
    n=len(arr)
    lst=[]
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==5:
                lst.append((arr[i],arr[j]))
                          
    return lst
            
                
arr=[1,2,3,4,5]
print(findans(arr))