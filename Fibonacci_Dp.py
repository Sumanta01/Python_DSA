# -*- coding: utf-8 -*-
"""
Created on Sun May 14 01:42:36 2023

@author: KIIT
"""
f=[0,1]
def Fibbo(n):
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
        
    return f[n]


print(Fibbo(8))
    
    