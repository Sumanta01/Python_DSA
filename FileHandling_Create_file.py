# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 02:52:58 2023

@author: KIIT
"""
import os

file=open("NLP_Copy.txt","w")
file.write("Data refers to information or facts that are collected, stored, and processed in a structured or unstructured format. It can be in the form of numbers, text, images, videos, or any other type of digital representation.")
file.close()

file=open("NLP_Copy.txt","r")
print(file.read())
file.close()

file2=open("NLP_Copy2.txt","w")
file2.write(" AI, or Artificial Intelligence, refers to the development of computer systems that can perform tasks that typically require human intelligence. It encompasses various techniques such as machine learning, natural language processing, and computer vision. AI has wide-ranging applications, from virtual assistants and autonomous vehicles to healthcare and finance.")
file.close()

file2=open("NLP_Copy2.txt","r")
print(file2.read())
file2.close()