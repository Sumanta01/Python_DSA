# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 16:03:56 2024

@author: KIIT
"""

def solve(st,ind,output,ans):
    if ind>=len(st):
        ans.append(output)
        return
    
    solve(st, ind+1, output, ans)
    output+=st[ind]
    solve(st,ind+1,output,ans)
    output=output[:-1]

def subsequence(st):
    ans=[]
    output=""
    ind=0
    solve(st,ind,output,ans)
    return ans

if __name__=="__main__":
    st=input()
    ans=subsequence(st)
    for i in ans:
        print(i,end=" ")