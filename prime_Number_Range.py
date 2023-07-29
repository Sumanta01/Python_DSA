# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 18:42:48 2023

@author: KIIT
"""

beg=int(input("Enter the starting number:"))
end=(int(input("Enter the ending number:")))

for i in range(beg,end):
    ct=0
    for j in range(2,int(i//2)):
        if i%j==0:
            ct+=1
            break
        
        
    if ct==0:
     print(i,end=" ")
       
        
