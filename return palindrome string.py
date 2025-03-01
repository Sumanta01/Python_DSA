# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 00:24:57 2023

@author: KIIT
"""

# String -> mamal return-> mam

def returnPalindrome(st):
    rev=''.join(reversed(st))
    ans=""
    for i in range(0, len(st)):
        for j in range(0,len(rev)):
            if st[i]==rev[j] and i==j:
                ans+=st[i]
                
    return ans
                




inp=input()
print(returnPalindrome(inp))