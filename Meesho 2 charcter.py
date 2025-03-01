# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:52:53 2024

@author: KIIT
"""

s = input()
chVal = input()
l = []
k = int(input())
for i in s:
    l.append(chVal[ord(i)-ord('a')])
i = 0
for j in range(len(l)):
    if (l[j] == '0'): k -= 1
    if (k < 0):
        if l[i] == '0':
            k += 1
        i += 1
print(j+1-i)


