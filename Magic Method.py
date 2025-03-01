# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 02:57:17 2023

@author: KIIT
"""

class Person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    
    def __del__(self):
        print("Object is being deconstructed !")

p=Person("Sumanta",22)
#print(p)