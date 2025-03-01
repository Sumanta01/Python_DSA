# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 18:29:45 2023

@author: KIIT
"""

def genSubArr(arr):
    ans=[]
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)+1):
            sub=arr[i:j]
            ans.append(sub)
            
    return ans


inp=list(map(int, input().split()))
res=genSubArr(inp)
for i in res:
    print(i,end="")