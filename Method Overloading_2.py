# -*- coding: utf-8 -*-
"""
Created on Mon May 22 00:51:45 2023

@author: KIIT
"""

class Overloading:
    
    def area(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
        print("Area is :",a*b*c)
        
        
    def area(self,a,b):
        self.a=a
        self.b=b
        
        print("Area is :",a*b)
        
        

ov=Overloading()
ov.area(32, 21)
#ov.area(31,39,25)
