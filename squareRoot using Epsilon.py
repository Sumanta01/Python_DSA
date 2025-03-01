# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 17:58:44 2024

@author: KIIT
"""
epsilon=1e-6
def squareRoot(n,epsilon):
    
    if n<0:
        return -1
    if n<2:
        return n
    
    beg=0.0
    end=n
    while end-beg>epsilon:
        mid=beg+(end-beg)/2.0
        square=mid*mid
        if square==n:
            return mid
        
        if n>square:
            beg=mid
        
        else:
            end=mid
            
    return beg


n=int(input())
ans=squareRoot(n,1e-6)
print("{:.3f}".format(ans))
        
    