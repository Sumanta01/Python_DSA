# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 00:21:58 2023

@author: KIIT
"""

def missingNumber(arr):
    n=len(arr)+1
    sum=0
    totalsum=(n*(n+1))//2
    for i in range (len(arr)):
        sum+=arr[i]
        
    missNum=totalsum-sum
    
    return missNum


if __name__=='__main__':
    num=[1,3,4,5,7,6]
    print(missingNumber(num))
    
