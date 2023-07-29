# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 21:46:51 2023

@author: KIIT
"""

def reverseString(str: str) -> str:
    val=str.split(" ")
    res=""
    val.reverse()
    for i in val:
        res+=i
        res+=" "
        
    return res
    

    
    



st="How are you"
print(reverseString(st))
         
    
    