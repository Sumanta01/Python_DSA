# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 17:09:22 2023

@author: KIIT
"""

list1=[1,2,3,5,5,6,2,76,98,21]
myset=set(list1)
print(myset)
myset.update({11,22,33})
print(myset)
#myset.remove(989)
myset.discard(989)
myset.pop()
myset.pop()
print(myset)
myset2=({11,2,3,4,5,6})
myset3=({2,3,7,9})
myset4=myset2 | myset3 #union
print(myset4)
myset4=myset2.intersection(myset3) #intersection
print(myset4)
myset4=myset2.difference(myset3) # set difference
print(myset4)

