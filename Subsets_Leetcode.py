# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 15:40:13 2024

@author: KIIT
"""
def solve(num,ind,ans,output):
    #base case
    if ind>=len(num):
        ans.append(output[:])
        return
    # recursive case
    # exclude
    solve(num, ind+1, ans, output)
    output.append(num[ind])
    #include
    solve(num, ind+1, ans, output)
    
    output.pop()

def genSubsets(num):
    ans=[]
    output=[]
    ind=0
    solve(num,ind,ans,output)
    return ans

if __name__=="__main__":
    num=list(map(int ,input().split()))
    res=genSubsets(num)
    for i in res:
        print(i, end="")