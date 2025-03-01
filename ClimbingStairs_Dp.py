# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 19:19:21 2023

@author: KIIT
"""

def ClimbingStairs(n):
    if n<=2:
        return n

    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
        
    return dp[n]



n=int(input())
print(ClimbingStairs(n))