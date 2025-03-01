# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:49:14 2024

@author: KIIT
"""

def findMinFreq(st):
    ans=[]
    for i in st:
        ans.append(st.count(i))
        
    print(st[ans.index(min(ans))])
    
    
s=input()
findMinFreq(s)