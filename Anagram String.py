# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 00:23:11 2024

@author: KIIT
"""

def isAnagram(st1,st2):
    st1=st1.lower();
    st2=st2.lower()
    
    st1=st1.replace(" ","")
    st2=st2.replace(" ","")
    
    sorted_st1=sorted(st1)
    sorted_st2=sorted(st2)
    
    if(sorted_st1==sorted_st2):
        return True
    else:
        return False;
    
    
str1=input()
str2=input()
print(isAnagram(str1, str2))