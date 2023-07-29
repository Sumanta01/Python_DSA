# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 23:02:00 2023

@author: KIIT
"""

class A:
    def run(self):
        print("Running")
        
        
class B:
    def start(self):
        print("Started>>>")
        
        
        
class C(A,B):
    def sound(self):
       self.run()
       self.start()
        
        

c=C()
c.sound()