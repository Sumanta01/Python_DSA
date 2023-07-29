# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 01:22:26 2023

@author: KIIT
"""
def sum1(n):
    return (n*(n+1)//2)



def sum2(n):
    sm=0
    for i in range(1,n+1):
        sm+=i;
    return sm;


x=(int(input()))
while(x):
    n=int(input())
    print(sum1(n))
    print(sum2(n))
    x-=1
    

        