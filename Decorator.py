# -*- coding: utf-8 -*-
"""
Created on Mon May 22 19:47:14 2023

@author: KIIT
"""

def hey_decorator(fun):
    
    def iner_fun():
        print("I am first")
        
        fun()
        
        print("I am second")
        
    return iner_fun


def ohh_noo():
    print("Ohh no i am third ")
    
    
ohh_noo=hey_decorator(ohh_noo)

ohh_noo()