# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 02:48:19 2023

@author: KIIT
"""

def isNumber(st):
    d_sum=0
    count=0
    
    for i in st:
        if i.isdigit():
            d_sum+=int(i)
            count+=1
            
    if count>0:
        d_avg=d_sum/count
    
    else:
        d_avg=0
        
    print("Sum is: ",d_sum)
    print("Avg is: ",d_avg)


st=input()
isNumber(st)
        
        
            
    