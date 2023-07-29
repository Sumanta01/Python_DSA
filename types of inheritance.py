# -*- coding: utf-8 -*-
"""
Created on Wed May 24 19:25:30 2023

@author: KIIT
"""
# single inheritance
# multilevel inheritance
# Multiple inheritance
class Road:
    
    def surface(self):
        print("The surface of the that road is very clean ...")
        
        
class Highway:
    def wide(self):
        print("The wide of highway is pretty good !..")
        

class Drain(Highway,Road):
    def clean(self):
        print("Yaa the drain is always clean and its area are good vibe..?")
        

d=Drain()
d.surface()
d.wide()
d.clean()
