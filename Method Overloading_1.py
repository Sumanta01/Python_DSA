# -*- coding: utf-8 -*-
"""
Created on Mon May 22 00:43:20 2023

@author: KIIT
"""

class Student_1:
    def name(self):
        print("Name is : Sumanta")
        
    def grade(self):
        print("B grade")
        
    def Roll(self):
        print("Roll no is : 85")
        
    
        

class Student_2:
    def name(self):
        print("Name is :Moody")
        
    def grade(self):
        print("A grade")
        
    def Roll(self):
        print("Roll no is : 35")


def fo(ob):
    ob.name()
    ob.grade()
    ob.Roll()
    
        
        
St1=Student_1()
st2=Student_2()      

fo(St1)
fo(st2)
        