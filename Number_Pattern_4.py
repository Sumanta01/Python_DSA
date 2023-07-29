# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 18:17:26 2023

@author: KIIT


"""
'''
Input N=4

Output :1
        11
        121
        1221
    
    '''

def numberPattern(n):

   
    res=[[]for k in range(n)]
    for i in range(n):
        ans=""
        for j in range (i+1):
            if j==0 or j==i:
                ans=ans+"1"
            else:
                ans=ans+"2"
        res[i].append(ans)
    return res

print(numberPattern(4))