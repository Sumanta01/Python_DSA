# -*- coding: utf-8 -*-
"""
Created on Thu May 25 19:25:33 2023

@author: KIIT
"""

class Animal:
    
    def __init__(self):
        
        print("Constructor is called,,,,,,,,,,,,,,,,")
        
            
    def horse(self):
        print("I am a horse and i want to race ........")
        
a=Animal()
a.horse()
print("%%%%%%%%%%%%%%%%")
print("******************")
print("@@@@@@@@@@@@@@@@@@@")
del (a)
b=Animal()
print(b)
del b
