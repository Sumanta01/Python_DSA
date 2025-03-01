# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 01:18:36 2023

@author: KIIT
"""

def FizzBuzz(n):
    for i in range(1,n+1):
        ans=""
        if i%3==0:
            ans+="Fizz"
        if i%5==0:
            ans+="Buzz"
        if i%7==0:
            ans+="Bazz"
        
        print(ans or i)
        
        
if __name__=="__main__":
    n=int(input())
    FizzBuzz(n)