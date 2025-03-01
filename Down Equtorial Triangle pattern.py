# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 02:12:44 2023

@author: KIIT
"""

def Pattern(n):
    for i in range(0,n):
        for j in range(0,i):
            print(" ",end="")
        for k in range(2*i,n+1):
            print("*",end="")
            
        print()
    
    

n=int(input())
Pattern(n)