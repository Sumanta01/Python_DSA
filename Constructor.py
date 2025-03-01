# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 17:26:22 2023

@author: KIIT
"""

class Dog:
    def __init__(self ,name ,age):
        self.name=name
        self.age=age
        
        
    def bark(self):
        print(f"{self.name} Bhoo Wohhh...")
        
        
d=Dog('Huskiee',7)
d2=Dog('Lab',6)

d.bark()
d2.bark()
print(f"{d.name} and his age is {d.age}")
print(f"{d2.name} and his age is {d2.age}")