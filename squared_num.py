# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 22:39:22 2022

@author: KIIT
"""

def get_Squared_Numbers(num):
    squared_numbers=[]
    for i in num:
        squared_numbers.append(i*i)
    return squared_numbers
  
num=[2,4,6,8]
print(get_Squared_Numbers(num))



# time complexity --> o(n)