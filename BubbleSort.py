# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 20:00:13 2023

@author: KIIT
"""

def BubbleSort(arr):
    for i in range(0,len(arr)):
        count=0
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                count+=1
        
        if count==0:
            return 1
    
    return 1

inp=[21, 2, 45, 32, 14, 29, 38, 4, 17]
ans=BubbleSort(inp)
if ans==1:
    for i in range(0,len(inp)):
        
        print(inp[i],end=" ")
        
else:
    print(-1) 
                
        