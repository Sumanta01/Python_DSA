# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 02:27:53 2023

@author: KIIT
"""

def mirrorString(st,n):
    
    alpha="abcdefghijklmnopqrstuvwxyz"
    rev_alpha=alpha[::-1]
    my_dict=dict(zip(alpha,rev_alpha))
    
    first=st[0:n-1]
    second=st[n-1:]
    
    mirror=""
    for i  in range(0,len(second)):
        mirror+=my_dict[second[i]]
        
    res=first+mirror
    
    return res

if __name__=="__main__":
    inp_str=input()
    inp_len=int(input())
    print(mirrorString(inp_str,inp_len))
        
    