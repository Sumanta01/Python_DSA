# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 16:37:45 2023

@author: KIIT
"""

''' *args vs *kwargs
'''

def multi(n,n2):
    return n*n2;

print(multi(9,5))

# *args
def multi2(*n):
    pro=1;
    for i in (n):
        pro=pro*i
    return pro

print(multi2(3,3,3,3,3,3,3,3,3,3))

# **kwargs

def wordOfSentence(**s):
    sent=''
    for i in s.values():
        sent+=i;
    
    return sent


print(wordOfSentence(a='Sumanta',b=' Swain ',c='fuck '))
        
        
    

