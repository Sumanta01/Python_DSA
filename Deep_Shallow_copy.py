# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:19:33 2023

@author: KIIT
"""
"""
x=lambda x,y:x*y
print(x(54,32))
"""
# Shallow copy
from copy import copy ,deepcopy
my_list=[1,2,3,[5,8],4,0]
list_2=copy(my_list)
list_2[2]=7
list_2[3].append(88)
print(list_2)
print(my_list)

print("---------------------------------")
#Deepcopy
list_3=deepcopy(my_list)
list_3[1]=65
list_3[3].append(548)
print(list_3)
print(my_list)
