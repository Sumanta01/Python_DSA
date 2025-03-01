# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 23:23:14 2023

@author: KIIT
"""

def PowerOfNumber(n,po):
    if po==0:
        return 1
    return n*PowerOfNumber(n, po-1)


n,po=(map(int,input().split()))
print(PowerOfNumber(n, po))