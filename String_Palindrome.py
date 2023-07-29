# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:09:58 2023

@author: KIIT

"""
"""
def isPalindrome(s: str) -> bool:
    n=len(s)
    for i in range(n//2):
        if(s[i]!=s[n-1-i]):
            break
        
    return i==(n//2)-1
    
print(isPalindrome("Tiger"))

"""

def isPalindrome(s: str) -> bool:
    st=s[::-1]
    if(st==s):
        return True
    else:
        return False

print(isPalindrome('madam'))
print(isPalindrome('kiit'))