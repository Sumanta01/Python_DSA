# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:12:26 2023

@author: KIIT
"""

my_list=[2,4,5,8,9]
print(my_list)

square_list=[x**2 for x in my_list if x%2!=0]
print(square_list)

square_dict={x:x**2 for x in my_list if x%3!=0}
print(square_dict)