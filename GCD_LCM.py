# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 01:50:50 2023

@author: KIIT
"""


def gcd(x,y):
    if(x==0):
        return y
    return gcd(y%x, x)


def lcm(x,y):
    prod=x*y
    hcf=gcd(x, y)
    return prod//hcf


x=int(input())
while(x):
  n,m=map(int ,input().split())
  print('gcd :{}'.format(gcd(n,m)))
  print('lcm :{}'.format(lcm(n,m)))
  x-=1;
            