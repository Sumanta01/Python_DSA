# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 01:20:56 2023

@author: KIIT
"""

def kthLargest(arr, size, k):
    arr.sort()
    for i in range(0,len(arr)):
        return arr[k]


if __name__=='__main__':
    size=int(input())
    k=int(input())
    arr=[]
    for i in range(size):
        arr.append(int(input()))
        
        
    print(kthLargest(arr, size, k))
                   
    
        
        

    
    
