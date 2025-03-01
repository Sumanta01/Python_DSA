# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 01:40:10 2023

@author: KIIT
"""

def pyramidPattern(n):
    beg=1
    end=n-1
    
    for i in range(1,n+1):
        for j in range(1,end+1):
            print(" ",end=" ")
        
        for k in range(1,beg+1):
            print("*",end='')
            if k<beg:
                print(" ",end=" ")
                
        print()
        beg+=1
        end-=1
        
        
inp=int(input())
pyramidPattern(inp)