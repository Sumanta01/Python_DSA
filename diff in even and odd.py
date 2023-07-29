# -*- coding: utf-8 -*-
"""
Created on Sun May 21 22:17:45 2023

@author: KIIT
"""

n=int(input())
l=[int (i) for i in input().split()]
    

even=0
odd=0
for i in l:
    if i&1:
        odd+=i
        
    else:
        even+=i
        
print(even-odd)
    
    
