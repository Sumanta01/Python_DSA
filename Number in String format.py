# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 19:59:53 2023

@author: KIIT
"""

def sayDigit(n):
    if n<0:
        return 
    digit_words = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    res=''
    while(n>0):
        r=n%10
        res+=digit_words[r]+" "
        n//=10
        
    word=res.split()
    
    return ' '.join(reversed(word))

inp=int(input())
ans=sayDigit(inp)
print(ans)
            
            
            
            
            
            
            