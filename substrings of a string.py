# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 00:07:53 2024

@author: KIIT
"""

def find_Substrings(st):
    sub=[]
    for i in range(len(st)):
        for j in range(i+1,len(st)+1):
            sub.append(st[i:j])
            
    
    return sub


s=input()
print(find_Substrings(s))