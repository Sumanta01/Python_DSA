# -*- coding: utf-8 -*-
"""
Created on Mon May 22 00:24:47 2023

@author: KIIT
"""

class Animal:
    def __init__(self):
        print("Hey bro i am animal")
        
    def name(self):
        print("My name is very Special")
        
    
    def color(self):
        print("My color is invisible")
        
        

class Tiger(Animal):
    def __init__(self):
        super().__init__()
        print("Tiger hoon mai !")
        
    def name(self):
        print("Tiger")
    
    def color(self):
        print("Brown")
        
t=Tiger()
t.color()
t.name()
t.__init__()
    
