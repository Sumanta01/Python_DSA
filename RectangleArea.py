# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 19:30:12 2023

@author: KIIT
"""

class Rectangle:
    
   def getArea(self,a,b):
      
       return int(a)*int(b)



a, b=input().split()

p=Rectangle()
print(p.getArea(a,b))





