# -*- coding: utf-8 -*-
"""
Created on Mon May 22 18:46:34 2023

@author: KIIT
"""

lst1=[71,42,4,56,88,19,50,76,7,3]

n=len(lst1)

for i in range(0,n):
    
    for j in range(i+1,n):
        if lst1[i]>lst1[j]:
            lst1[i],lst1[j]=lst1[j],lst1[i]
            
            
print(lst1)