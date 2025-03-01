# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:11:04 2023

@author: KIIT
"""

x=int(input())
y=int(input())

for n in range(x,y+1):
    if(n>1):
        for i in range(2,n):
            if n%i==0:
                break
            
        else:
            print(n,end=" ")
    
    
    