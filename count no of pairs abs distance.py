# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 11:36:42 2024

@author: KIIT
"""



def countKDifference( nums, k):
    count=0
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]-nums[j]==k or nums[j]-nums[i]==k:
                count+=1
    
    return count
                
                

li=[1,2,2,1]
k=1
print(countKDifference(li, k))
     