# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 17:38:37 2023

@author: KIIT
"""

def multiply(a,b,*argv):
    mul=a*b
    for i in argv:
        mul*=i
    return mul

print(multiply(10,54,76,98,43))



def helloargue(**kwargs):
    for key ,value in kwargs.items():
        print(key+ ":" +value)
        
        
helloargue(arg1="Hii bro",arg2="Hii sis",arg3="Hii babe")