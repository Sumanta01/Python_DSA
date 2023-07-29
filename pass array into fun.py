# -*- coding: utf-8 -*-
"""
Created on Sat May 20 22:50:01 2023

@author: KIIT
"""

from array import *
sum=1.0

def why_not(arr):
    global sum
    for i in arr:
       sum*=i
           
           
        
    return(sum)
    
    


my_arr=[23,55,67,89,56,12,30,44,66]
print(why_not(my_arr))
        
    