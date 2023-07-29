# -*- coding: utf-8 -*-
"""
Created on Mon May 22 18:42:51 2023

@author: KIIT
"""

def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
        
f=fibonacci()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))  

'''
def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
        
g=fibonacci()

for i in g:
    print(i,end=" ")  '''