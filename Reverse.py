# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:03:05 2023

@author: KIIT
"""

def reverse_str(st):
    rev=st.split()
    rev_str=[i[::-1] for i in rev]
    ans=' '.join(rev_str)
    return ans
    
    
inp=input()
print(reverse_str(inp))