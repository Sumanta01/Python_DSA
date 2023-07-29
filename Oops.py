# -*- coding: utf-8 -*-
"""
Created on Mon May 22 00:14:21 2023

@author: KIIT
"""

class Animal:
    def __init__(self,age,color,name):
        self.age=age
        self.color=color
        self.name=name
        

tom=Animal(22, "white", "Cat")
blacky=Animal(33, "black", "Dog")
print("Tom is a {}".format(tom.name))
print("Blacky color is {}".format(blacky.color))

