# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 01:10:28 2023

@author: KIIT
"""

def generatedBinaryNumber(n):
    q=[]
    l=[]
    q.append("1")
    
    for i in range(n):
        temp=q.pop(0)
        l.append(temp)
        q.append(temp+"0")
        q.append(temp+"1")
        
    return l


print(generatedBinaryNumber(10))