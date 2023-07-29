# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 18:54:27 2023

@author: KIIT
"""

def duplicateElm(arr):
    see=set()
    visit=[]
    
    for i in arr:
        if i in see:
            visit.append(i)
            
        else:
            see.add(i)
            
            
    return list(see)



lst=[1,2,3,4,2,1,5,6,3]
print(duplicateElm(lst))