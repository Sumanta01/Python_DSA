# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 16:48:51 2023

@author: KIIT
"""

n=int(input("Enter the number :"))
ct=0
for i in range(2,int(n//2)):
    if n%i==0:
        ct+=1
        break;
        
if(ct==0):
    print("prime")
else:
    print("Not prime")
    
    
