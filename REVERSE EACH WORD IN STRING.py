# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:20:00 2023

@author: KIIT
"""

def reverseWord(st):
    
    word=st.split()
    ans=' '.join(word[::-1])
        
    return ans


inp="Happy hours to be Coding"
print(reverseWord(inp))
        
    
    

'''
def reverseword(st):
    ans=""
    word=st.split()
    for i in word:
        ans+=i[::-1]+" "
        
    return ans


inp_str="Sumanta is a good coder"
print(reverseword(inp_str))  '''