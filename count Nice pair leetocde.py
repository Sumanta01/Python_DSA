# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 12:59:42 2024

@author: KIIT
"""


def countNicePairs(nums):
    
    def reverseNum(n):
        rev=0
        while n>0:
            r=n%10
            rev=rev*10+r
            n//=10
        
        return rev
    
    count=0
    constraint=10**9+7
    mp={}
    for i in nums:
        rev=reverseNum(i)
        diff=i-rev
        
        count=(count + mp.get(diff,0))%constraint
        mp[diff]=mp.get(diff,0)+1
        
    return count
    
if __name__=="__main__":
    li=[42,11,1,97]
    print(countNicePairs(li))