# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:57:09 2023

@author: KIIT

"""

'''

Input N=4
Output :
    1
    11
    111
    1111
    11111
    
    '''
    
# Time Complexity O(N)

def printPattern(n):
    s="1"

    for i in range(n):
        print(s)
        s=s+"1"
    pass


printPattern(6)
## Another Approach Time Complexity O(N^2)
def printPattern(n):
    for i in range(n):
        for j in range(i+1):
            print('1',end="")
        print()
    pass


printPattern(6)
'''
def printPattern(n):
    i=1
    while(i<=n):
        print(i*"1")
        i+=1

printPattern(4)
'''





