# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 18:49:27 2023

@author: KIIT
"""

def primeFact(n):
    fact=[]
    while(n%2==0):
        fact.append(2)
        n//=2
        
    i=3
    while(i<=n):
        while(n%i==0):
            fact.append(i)
            n//=i
            
        i+=2
        
    if(n>2):
        fact.append(n)
        
    return fact

if __name__=="__main__":
    n=int(input())
    res=primeFact(n)
    print(res)