# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 02:00:01 2023

@author: KIIT
"""

def palindromeSubstring(st):
    res=[]
    ans=[]
    count=0
    for i in range(0,len(st)):
        for k in range(i+1,len(st)+1):
            sub=st[i:k]
            res.append(sub)
            
    
    rev=[i[::-1] for i in res]
    
    for i in range(0,len(res)):
        if rev[i]==res[i]:
            ans.append(res[i])
            count+=1
            
    return count,ans


inp=input()
res=palindromeSubstring(inp)
for i in res:
    print(i)