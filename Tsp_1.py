# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:51:25 2023

@author: KIIT
"""

n = 4  
dist = [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [
    0, 10, 0, 25, 25], [0, 15, 25, 0, 30], [0, 20, 25, 30, 0]]
 

memo = [[-1]*(1 << (n+1)) for _ in range(n+1)]
 
 
def fun(i, man):
   
    if man == ((1 << i) | 3):
        return dist[1][i]
 
    # memoization
    if memo[i][man] != -1:
        return memo[i][man]
 
    res = 10**9  
    for j in range(1, n+1):
        if (man & (1 << j)) != 0 and j != i and j != 1:
            res = min(res, fun(j, man & (~(1 << i))) + dist[j][i])
    memo[i][man] = res  
    return res
 
 

result = 10**9
for i in range(1, n+1):
   
    result = min(result, fun(i, (1 << (n+1))-1) + dist[i][1])
 
print("The cost of most efficient tour = " + str(result))