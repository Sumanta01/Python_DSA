# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 06:02:35 2023

@author: KIIT
"""

#24=[1,2,3,4,6,8,12,24]


from math import *

def fun2(n):
    div2=set()
def fun1(n):
    div1=[]
    for i in range(1,n+1):
        if(n%i==0):
            div1.append(i)
    return div1
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            div2.add(i)
            div2.add(n//i)
    return list(div2)

t=int(input())
while(t):
    n=int(input())
    div1=fun1(n)
    print(*div1)
    div2=fun2(n)
    print(*div2)
    t-=1
    