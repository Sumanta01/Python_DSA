# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 02:29:41 2023

@author: KIIT
"""

import os

# Read the file
'''
file=open("NLP.txt","r")
print(file.read())
print(file.read(23))
file.close() '''
'''
file=open("NLP.txt","a") #write file in append mode
file.write("\n How the Model is trained well by NLP ?")
file.close()


file=open("NLP.txt")
print(file.read())
file.close()
'''

file=open("NLP.txt","w") #write file in write mode
file.write("\n How the Model is trained well by NLP ?")
file.close()


file=open("NLP.txt")
print(file.read())
file.close()



