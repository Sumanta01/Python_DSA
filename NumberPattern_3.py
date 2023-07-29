# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 18:10:37 2023

@author: KIIT

"""
'''

Input N=3

Output: 1
        23
        345
        4567
        
'''
def numberPattern(n):
	res=[]
	# Write Your code here.
	for i in range(n):
		x=i+1
		s=""
		for j in range(i+1):
			s=s+str(x)
			x+=1
		res.append(s)
	return res

print(numberPattern(4))