# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 01:42:30 2023

@author: KIIT
"""

def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
        
        else:
            return True
        
        
res=filter(prime, range(10))
print(list(res))