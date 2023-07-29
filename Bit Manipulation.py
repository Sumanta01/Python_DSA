# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 18:09:09 2023

@author: KIIT
"""

# BitWise AND
a=33
b=21
print(a & b)

# Bitwise OR
print(a|b)

#Left Shift operator
g=18
print(g<<2)

#Right Shift Operator

u=18
print(u>>2)

# NOT 

h=15
y=-14
print(~h)
print(~y)

'''
#Even Odd
num=int(input())
if num & 1>0:
    
    print( "Odd")

else:
    print ("Even") '''
    
#Check  number 2s Power

num=int(input())
if num & (num-1)==0:
    print("Yes")
    
else:
    print("No")













