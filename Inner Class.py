# -*- coding: utf-8 -*-
"""
Created on Fri May 26 17:51:30 2023

@author: KIIT
"""

class Language:
    
    def __init__(self):
        self.Language="Python"
        self.lang=self.stream()
        
    def show(self):
        print("The language is :",self.Language)
        
    class stream:
        def __init__(self):
            self.type="Interpreted!!"
            self.created=1991
        def display(self):
            print("The type is :",self.type)
            print("Created in :",self.created)
            
            
            
Lan=Language()
Lan.show()
pin=Lan.lang
pin.display()
            
    