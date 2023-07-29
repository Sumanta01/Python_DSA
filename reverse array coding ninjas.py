# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 11:47:28 2023

@author: KIIT
"""

def reversepoint(arr,n):
    return arr[0:n+1]+arr[-1:n:-1]




arr=[1,2,3,4,5,6]
n=3
print(reversepoint(arr, n))