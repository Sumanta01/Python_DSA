# -*- coding: utf-8 -*-
"""
Created on Sun May 28 23:28:25 2023

@author: KIIT
"""

class University:
    
    def __init__(self):
        print("University is created ...")
        
    def show(self):
        print("University is very Beautiful")
        
        
class College(University):
    
    def look(self):
        print("College are under the university Guideline")
        

class  School(College,University):
    
    def work(self):
        print("School is the base of the student's career...")
        
        
        
S=School()
S.look()
S.show()
S.work()
    