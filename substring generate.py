 # -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 00:41:05 2023

@author: KIIT
"""

def generateSubstring(st):
    ans=[]
    for i in range(0,len(st)):
        for j in range(i+1,len(st)+1):
            sub=st[i:j]
            ans.append(sub)
            
    return ans
            
            
        

inp_str=input()
res=generateSubstring(inp_str)

for i in res:
    print(i)
    
    
    
'''def generateSubstr(st):
    return [st[i:j] for i in range(len(st)) for j in range(i+1,len(st)+1)]


inp=input()
res=generateSubstr(inp)
for i in res:
    print(i)  '''
