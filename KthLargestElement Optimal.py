# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 02:42:38 2024

@author: KIIT
"""
import heapq

def kthLargestElement(nums,k):
    minHeap=[]
    for i in nums:
        heapq.heappush(minHeap, i)
        if len(minHeap)>k:
            heapq.heappop(minHeap)
            
    return minHeap[0]




num=[21, 2, 32 ,44 ,19 ,4, 98]
k=2
print(kthLargestElement(num, k))