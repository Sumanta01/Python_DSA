# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 02:51:13 2023

@author: KIIT
"""

def mergeString(st1,st2):
    ans=""
    for i,j in zip(st1,st2):
        ans+=i+j
        
    return ans
        
        
        
    
st1=input()
st2=input()
print(mergeString(st1, st2)) #apbqcr
        