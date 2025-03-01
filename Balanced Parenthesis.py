# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:08:03 2023

@author: KIIT
"""

def isValid(s):
    stack=[]
    for i in s:
        if  i in '{[(':
            stack.append(i)
            
        elif i=='}':
            if stack and stack[-1]=='{':
                stack.pop()
            else:
                return False
            
        
        elif i==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                return False
            
        elif i==']':
            if stack and stack[-1]=='[':
                stack.pop()
                
            else:
                return False
            
    return len(stack)==0


if __name__=="__main__":
    str_input=input()
    if(isValid(str_input)):
        print("Valid String")
    else:
        print("Invalid String")
        
        