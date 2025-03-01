# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 01:40:09 2024

@author: KIIT
"""

def longest_increasing_subsequence(arr):
    n = len(arr)
    
    # Initialize an array to store the length of the longest increasing subsequence
    lis = [1] * n
    
    # Iterate through the array
    for i in range(1, n):
        for j in range(0, i):
            # Check if the current element can be added to the increasing subsequence
            if arr[i] > arr[j] and (arr[i] - arr[j]) > (i - j):
                lis[i] = max(lis[i], lis[j] + 1)
    
    # Return the maximum length of the increasing subsequence
    return max(lis)

# Example usage
arr = [1, 5, 7, 10, 15, 20]
result = longest_increasing_subsequence(arr)
print("Length of the longest increasing subsequence:", result)
