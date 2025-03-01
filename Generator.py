# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 02:42:50 2023

@author: KIIT
"""

def myGenerator(n):
    for i in range(n):
        yield i**3
        
res=myGenerator(9888888888)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
