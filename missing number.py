# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 19:54:25 2023

@author: KIIT
"""

def firstMissing(arr, n):
   i=0
   while i<n:
       cor=arr[i]
       if(arr[i]<n and arr[i]!=arr[cor]):
           swap(arr,i,cor)
           
       else:
           i+=1
           
   for j in arr:
       if arr[j]!=j:
           
           return j
    
   return n
       


def swap(arr,i,cor):
    arr[i],arr[cor]=arr[cor],arr[i]
    
    
           
arr=[0 ,1 ,2 ,3, 4]
n=len(arr)

print(firstMissing(arr, n))

           
           
   
           
           
   

           
           
   
           
   
 

          
          
        
               
           
    
    
           
