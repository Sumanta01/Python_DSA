# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 15:25:55 2023

@author: KIIT
"""
# Create a new File
#f=open('Code.txt','x')
#f.close()

# Write inside the file 
f=open('Code.txt','a')
#f.write("n=int(input()) rev=int(str(n)[::-1]) print(rev)")
f.close()


# open to read the file
f=open('Code.txt','r')
print(f.read(5))