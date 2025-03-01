# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 03:04:01 2023

@author: KIIT
"""

class Vector:
    
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
    def __add__(self,other):
        return Vector(self.x + other.x,self.y + other.y)
    
    def __repr__(self):
        return f"X: {self.x},Y:{self.y}"
    
    def __call__(self):
        print ("Hello! I was called !")
    
v1=Vector(22, 55)
v2=Vector(44, 23)
v3=v1+v2
print(v3)
v3()