# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 18:08:14 2023

@author: KIIT
"""

def search(nums: [int], target: int):
   def binary(beg,end):
       if beg>end:
           return -1
       
       
       mid=beg+(end-beg)//2
       if nums[mid]==target:
           return mid
       elif target>nums[mid]:
           return binary(mid+1, end)
       
       
       return binary(beg, mid-1)
   
    
   return binary(0, len(nums)-1)
       
        
        



nums=[12,34,76,87,231,432,654]
target=432

print(search(nums, target))
