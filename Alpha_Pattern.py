# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:33:10 2023

@author: KIIT
"""

def AlphaPattern(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(ord('A')+i),end='')
        print()
        
        

n=int(input())
AlphaPattern(n)