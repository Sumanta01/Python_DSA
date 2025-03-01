# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:50:39 2024

@author: KIIT
"""
import heapq

def findKthElement(arr,k):
    heap=[]
    for i in arr:
        heapq.heappush(heap, i)
        
        if(len(heap)>k):
            heapq.heappop(heap)
            
    return heap[0]
        
    
arr=[32,3,443,322,12,87,54,76]
k=3
for i in range(1,k+1):
    print(findKthElement(arr, i))
    
print()
print(findKthElement(arr, k))