# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 22:50:10 2023

@author: KIIT
"""

from collections import *


def pushAtBottom(myStack: deque, x: int):
    temp_stack=[]
    while len(myStack)>0:
        temp_stack.append(myStack.pop())
        
    myStack.append(x)
    
    while len( temp_stack)>0:
        myStack.append(temp_stack.pop())
    
    
    return myStack



stack = [1, 2, 3, 4]
x=5

print(pushAtBottom(stack, x))


