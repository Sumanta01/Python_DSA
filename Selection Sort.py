# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 00:37:14 2023

@author: KIIT
"""

def selectionSort(arr):
    for i in range(0,len(arr)):
        min_ele=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_ele]:
                min_ele=j
                
        arr[i],arr[min_ele]=arr[min_ele],arr[i]
        
    for i in range(0,len(arr)):
        print(arr[i],end=" ")
        
        

inp=[54,22,5,12,18,32,41,76]
selectionSort(inp)
        