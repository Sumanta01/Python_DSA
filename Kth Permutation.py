# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 02:25:34 2023

@author: KIIT
"""

def KthPermutation(N,K):
    inp=list(range(1,N+1))
    res=[]
    fact=calculate_factorial(N)
    K=K-1
    
    for i in range(N,0,-1):
        fact=fact//i;
        index=K//fact
        K=K%fact
        
        ans_inp=inp.pop(index)
        res.append(ans_inp)
        
    return res


def calculate_factorial(n):
    if n==0 or n==1:
        return 1
    return n*calculate_factorial(n-1)


if __name__=='__main__':
    N=int(input())
    K=int(input())
    res=KthPermutation(N, K)
    print(res)