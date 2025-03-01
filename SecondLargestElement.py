# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:05:52 2023

@author: KIIT
"""

def findSecondLarge(arr):
    first_large=second_large=float('-inf')
    for i in range(0,len(arr)):
        if arr[i]>first_large:
            second_large=first_large
            first_large=arr[i]
            
        elif (arr[i]>second_large and arr[i]!=first_large):
            second_large=arr[i]
            
    return second_large



if __name__=='__main__':
    li=[22,32,4,54,12,5,98,21]
    print(findSecondLarge(li))