# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 01:15:13 2023

@author: KIIT
"""

def Merge_Sort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left=Merge_Sort(arr[mid:])
    right=Merge_Sort(arr[:mid])
    
    return merge(left,right)


def merge(left,right):
    merg=[]
    i=j=0
    while(i<len(left) and j<len(right)):
        if left[i]<=right[j]:
            merg.append(left[i])
            i+=1
            
        else:
            merg.append(right[j])
            j+=1
            
    merg+=left[i:]
    
    merg+=right[j:]
    
    return merg


if __name__=='__main__':
    arr=[12,4,21,1,43,15,8]
    sort_arr=Merge_Sort(arr)
    print(sort_arr)
            
    