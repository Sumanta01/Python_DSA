# -*- coding: utf-8 -*-
"""
Created on Wed May 24 19:47:39 2023

@author: KIIT
"""
# Data Mangling

class Card:
    
    def __init__(self,cardNo):
        self.__cardNo=cardNo  #private attribute
        
    
    def uses(self):
        print(f"debit card number of {self.__cardNo} is used")
        
        
c=Card(63538764)
c.uses()
print(c._Card__cardNo)