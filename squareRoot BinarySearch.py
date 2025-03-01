# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 18:13:58 2024

@author: KIIT
"""

def squareRoot(n):
    if n<2:
        return n
    
    beg,end=0,n
    while beg<=end:
        mid=beg+(end-beg)//2
        if mid*mid ==n:
            return mid
        if n>mid*mid:
            beg=mid+1
        else:
            end=mid-1
            
    return end


n=int(input())
print(squareRoot(n))
