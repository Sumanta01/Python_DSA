# -*- coding: utf-8 -*-

"""
Created on Tue Oct 17 11:32:52 2023

@author: KIIT
"""

def digitSum(s):
    d_sum=0
    count=0
    for c in s:
        if c.isdigit():
            d_sum+=int(c)
            count+=1
            
    if count>0:
        d_avg=d_sum/count
        
    else:
        d_avg=0
        
    print("Sum: ",d_sum)
    print("Avg: ",d_avg)
        

if __name__=='__main__':
    st="Sumanta123 Swain654"
    digitSum(st)
    
    