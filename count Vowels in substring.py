# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 23:57:32 2024

@author: KIIT
"""

def count_Vowel_Substrinngs(st):
    vowels="aeiouAEIUO"
    vowelCount=0
    for i in range(len(st)):
        for j in range(i+1,len(st)+1):
            subStr=st[i:j]
            vowelCount+=sum(1 for char in subStr if char in vowels) 
            
    
    return vowelCount


st=input()
print(count_Vowel_Substrinngs(st))



