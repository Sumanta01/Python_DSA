# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 19:07:31 2023

@author: KIIT
"""

def sort_char(string):
    ch_str=list(string)
    n=len(string)
    for i in range(0,n):
        for j in range(0,n-1-i):
            if ch_str[j]>ch_str[j+1]:
                ch_str[j],ch_str[j+1]=ch_str[j+1],ch_str[j]
                
    sort_str=''.join(ch_str)
    return sort_str

if __name__=="__main__":
    input_str=input()
    print(sort_char(input_str))