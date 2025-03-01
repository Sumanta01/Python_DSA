# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 00:54:48 2023

@author: KIIT
"""

def repeatCharString(st):
    charCount={}
    
    for i in st:
        if i in charCount:
            charCount[i]+=1
        else:
            charCount[i]=1
            
    for i,char in enumerate(st):
        if charCount[char]==1:
            return i;
    
    return -1;



input_str=input()
print(repeatCharString(input_str))