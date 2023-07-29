# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 19:38:46 2023

@author: KIIT
"""

def sortLexo(my_string):
 
    
    words = my_string.split()
     
   
    words.sort()
 
    
    for i in words:
        print( i )
        
        

inp=input()

sortLexo(inp)
 