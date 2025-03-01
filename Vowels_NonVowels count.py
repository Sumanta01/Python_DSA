# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 12:51:12 2023

@author: KIIT
"""

def findVowelsNonVowels(inp):
    vowels="aeiouAEIOU"
    vow=[]
    non_vowel=[]
    count=0
    flag=0
    for i in inp:
        if i in vowels:
            vow.append(i)
            count+=1
            
        else:
            non_vowel.append(i)
            flag+=1
            
    return vow,non_vowel ,count ,flag


inp=input()
vow ,nonvow,count,flag=findVowelsNonVowels(inp)
print("Vowels :" ,vow)
print("NonVowels: ",nonvow)
print("Vowels Count :" ,count)
print("Non Vowels count : ",flag)