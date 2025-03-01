# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 23:51:47 2023

@author: KIIT
"""

def sieveOfErthunates(n):
    isPrime=[False]*n
    
    for i in range(2,n):
        if isPrime[i]==False:
            for j in range(i*i,n,i):
                isPrime[j]=True
                
    
    ans=[i for i in range(2,n) if isPrime[i]==False]
    return ans


n=int(input())
res=sieveOfErthunates(n)
print(res)