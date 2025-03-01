# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 23:51:55 2023

@author: KIIT
"""

def countAllPrevoiusNumber(n):
    if n==0:
        return
    print(n,end=' ')
    countAllPrevoiusNumber(n-1)

i=int(input())
countAllPrevoiusNumber(i)