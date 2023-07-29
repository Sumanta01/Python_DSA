# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 22:44:19 2022

@author: KIIT
"""

num=[12,3,12,4,56,5,7,4]
for i in range (len(num)):
   for j in range(i+1,len(num)):
       if(num[i]==num[j]):
           print(num[i] ,"is a duplicate number:")
          
            
          #Time complexity is: a*n^2+b*n+c --->o(n^2)
          
          