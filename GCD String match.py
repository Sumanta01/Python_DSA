# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 02:30:01 2023

@author: KIIT
"""

import math
def gcdStringMatch(st1,st2):
    
    if st1+st2!=st2+st1:
        return ""
    
    n=math.gcd(len(st1),len(st2))
    return st1[:n]


st1=input()
st2=input()
print(gcdStringMatch(st1, st2))

    