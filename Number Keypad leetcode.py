# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 17:31:00 2024

@author: KIIT
"""

def solve(digit ,ind,output,ans,mapping):
    if ind==len(digit):
        ans.append(output)
        return
    num=int(digit[ind])
    val=mapping[num]
    for i in range(0,len(val)):
        output+=val[i]
        solve(digit, ind+1, output, ans, mapping)
        output=output[:-1]
    

def numberKeypad(digit):
    ans=[]
    output=""
    if(len(digit)==0):
        return ans
    ind=0
    mapping=[" "," ","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    solve(digit, ind ,output ,ans, mapping)
    return ans
        
if __name__=="__main__":
    st=input()
    res=numberKeypad(st)
    for i in res:
        print(i,end=" ")
        
        