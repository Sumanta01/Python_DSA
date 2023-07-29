# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 18:20:56 2023

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
            
            
    return visit



awr = [1,22,3,1,22,23,22,54,87,34,21,76,54]
ans=duplicateElm(awr) 
print(ans)
    
  


