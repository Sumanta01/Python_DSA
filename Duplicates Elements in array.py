# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 14:14:18 2023

@author: KIIT
"""
# Experimental Analysis
import numpy as np
import time as t
beg=t.time()
arr=[1,2,3,2,4,5,4,8,7,5,6,9,6]
found=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            found=arr[i]
            print(found,end=" ")
            
            

end=t.time()
print()
print("Time {}:".format(3600*(end-beg)))
