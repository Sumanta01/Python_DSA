# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 19:38:03 2023

@author: KIIT
"""

def mydecaorator(function):

    def wrapper():
        function()
        print("I am decortaing the function !")
    
    return wrapper
        
@mydecaorator
def greet():
    print("Heyy welcome to advance python")
    

greet()