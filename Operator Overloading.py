# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 23:53:13 2024

@author: KIIT
"""

class vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __sub__(self,other):
        if isinstance(other, vector2D):
            return vector2D(self.x-other.x,self.y-other.y)
        else:
            raise TypeError()
        
    
    def __add__(self ,other):
        if isinstance(other,vector2D):
            return vector2D(self.x + other.x,self.y+other.y)
        
        else:
            raise TypeError()
            
            
    def __str__(self):
        return f"({self.x},{self.y})"
    

v1=vector2D(33, 79)
v2=vector2D(76,44)
v3=v1+v2
v4=v1-v2
print(v4)
print(v3)
