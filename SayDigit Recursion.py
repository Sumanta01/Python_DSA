# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 20:44:11 2023

@author: KIIT
"""

def sayDigit(n):
    if n<0:
        return n 
    if n==0:
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
    rem=n%10
    n//=10
    sayDigit(n)
    
    print(digit_words[rem],end=' ')
    

n=int(input())
sayDigit(n)
    
    