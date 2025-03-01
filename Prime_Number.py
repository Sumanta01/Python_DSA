# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 12:49:47 2023

@author: KIIT
"""

x=int(input())
count=0
for i in range(2,x):
    if x%i==0:
        count+=1
        break
    
if count==0:
    print(f"{x} is a prime number ")
    
else:
    print(f"{x} is not a prime number")
        