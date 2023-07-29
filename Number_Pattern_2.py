# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 17:22:10 2023

@author: KIIT

"""
'''

Input N=4
Output: 12345
        1234
        123
        12
        1
        
'''



def numberPattern(n):
    for i in range(n+2):
        for j in range(n-i):
            print(j+1,end='')
        print()
        
numberPattern(5)


def numberPattern(n):
	res=[]
	for i in range(n+1):
		s=""
		for j in range(n-i):
			s=s+str(j+1)
		res.append(s)
	return res

print(numberPattern(4))


    