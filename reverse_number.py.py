# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 01:06:49 2023

@author: KIIT
"""
x=(int(input()))
rev=0
while(x>0):
    r=x%10
    rev=rev*10+r
    x//=10
    
print(rev)
    
    
    
    