# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 00:31:45 2024

@author: KIIT
"""

from itertools import product

a=set(map(int,input().split()))
b=set(map(int,input().split()))

res=set(product(a,b))

for i in res:
    print(i, end=" ")