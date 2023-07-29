# -*- coding: utf-8 -*-
"""
Created on Sat May 13 23:39:19 2023

@author: KIIT
"""

def number(x):
    num=[0,1]
    for i in range(2,x):
       num.append(num[i-1]+num[i-2])
        
        
    return num[x-1]
    
    

if __name__ == "__main__":
    
    x=int(input())
    print(number(x))
    for i in range (2,x+1):
        print(number(i),end=" ") 
    
    

