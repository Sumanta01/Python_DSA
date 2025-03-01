# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 02:27:11 2023

@author: KIIT
"""

def Pattern(n):
    for i in range(0,n+1):
        for j in range(0,n-i):
            print(" ",end="")
            
        for k in range(0,(2*i-1)):
            print("*",end="")
            
        print()
        
        
n=int(input())
Pattern(n)