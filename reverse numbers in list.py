# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 12:02:52 2024

@author: KIIT
"""

def reverseNummberList(li):
    res=[]
    for i in li:
        ans=int(str(i)[::-1])
        res.append(ans)
        
    return res



inp=[21,32,45,87]
print(reverseNummberList(inp))
        