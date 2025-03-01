# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 13:14:49 2023

@author: KIIT
"""

def push(stack,i):
    stack.append(i)
    
    
def isEmpty(stack):
    if(len(stack)==0):
        return True
    else:
        return False
    
def Pop(stack):
    if(isEmpty(stack)):
        return 
    
    return stack.pop()



stack=[]
for i in range(5):
    
    push(stack,i)

print(stack)
print(Pop(stack))
print(stack)
print(isEmpty(stack))
    