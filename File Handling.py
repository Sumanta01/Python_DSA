# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 15:14:11 2023

@author: KIIT
"""

#f=open('Demo.txt','r')
#print(f.read())

#print(f.readline(10))

f=open('Demo.txt','a')
f.write(" ----->(Sumanta) How my luck playing with me Hey God please help me to find a good Job for me")
f.close()
f=open('Demo.txt','r')
print(f.read())
f.close()