# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 13:32:12 2023

@author: KIIT
"""

class Bus:
    def capacity(self):
        print("50 people around in bus")
        
    def color(self):
        print("White")
        
        
class Car:
    def capacity(self):
        print("5 people around in car ")
        
    def color(self):
        print("Red")
        
        
b=Bus()
c=Car()

for i in (b,c):
    i.capacity()
    i.color()
    print("------------")