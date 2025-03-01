# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 23:09:21 2023

@author: KIIT
"""

my_dict={}

while True:
    key=input("Enter the key (press enter to stop): ")
    
    if key=="":
        break
    
    value=input(f"Enter the value for {key}: ")
    
    my_dict[key]=value
    
print(my_dict)