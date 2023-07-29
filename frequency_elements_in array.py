# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 18:37:58 2023

@author: KIIT
"""

def frequency(arr):
    frequency_find={}
    
    for i in arr:
        if i in frequency_find:
            frequency_find[i]+=1;
            
        else:
            frequency_find[i]=1;
            
    return frequency_find



arr=[12,32,4,12,4,32,87,32,1,23,45]
print(frequency(arr))
            