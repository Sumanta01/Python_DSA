# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 12:31:41 2024

@author: KIIT
"""

def getSeatAllocation(arr):
    res={}
    ans={}
    q=[]
    for i in range(len(arr)):
        q.append([i+1,arr[i]])
    
    while q:
        p,s=q.pop(0)
        if s not in res:
            ans[p]=s
            res[s]=1
        else:
            q.append([p,s+1])
    
    flag=[]
    for i in range(len(arr)):
        flag.append(ans[i+1])
    return flag
    

arr=[1,3,3,2,2]
arr2=[1,1,1,1]
print(getSeatAllocation(arr2))
        