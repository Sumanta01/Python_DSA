# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 22:50:53 2023

@author: KIIT
"""

def reverseString(str: str) -> str:
    res=""
    for i in range(len(str)-1 ,-1,-1):
        
        res+=str[i]
        
    return res


    
        
    
    
    
st="How are you"
print(reverseString(st))