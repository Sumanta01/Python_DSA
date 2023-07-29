# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 18:59:16 2023

@author: KIIT
"""

import math

def findmin(arr):
    res=math.inf
    for i in arr:
        if i<res:
            res=i
            
    return res


arr=[11,2,3,5,-55,0,7,-4,21,73]
print(findmin(arr))

#print(max(arr))
#print(min(arr))
