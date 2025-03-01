# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 18:43:06 2023

@author: KIIT
"""

def Partition(arr,l,h):
    i=l-1;
    pivot=arr[h]
    for j in range(l,h):
        if arr[j]<pivot:
            i+=1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            
    i+=1
    temp=arr[i]
    arr[i]=pivot
    arr[h]=temp;
    
    return i;

def Quicksort(arr,l,h):
    if l <h:
        pivot=Partition(arr, l, h)
        Quicksort(arr, pivot+1, h)
        Quicksort(arr, l, pivot-1)
        
        
if __name__=="__main__":
    arr=[32,4,12,43,8,54,21,17,2]
    l=0
    h=len(arr)-1
    Quicksort(arr, l, h)
    for i in range(0,len(arr)):
        print(arr[i],end=" ")
            