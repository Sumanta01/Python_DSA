# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 02:03:51 2023

@author: KIIT
"""

def primeFact(n):
    i=2
    while i*i<=n:
        while n%i==0:
            n//=i;
            print(i,end=" ")
            
        i+=1
            
            
    if(n!=1):
        print(n,end=" ")
        
        
if __name__=="__main__":
    n=int(input())
    primeFact(n)
        