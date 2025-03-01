# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 19:05:30 2023

@author: KIIT
"""

Q=[]
l=None
r=None

def isEmpty(q):
    if Q==[]:
        return True
    
    else:
        return False
    
    
def enqueue(que , val):
    que.append(val)
    if len(que)==1:
        l=r=0
        
    else:
        r=len(que)-1
        
        
def dequeue(q):
    if isEmpty(q)==True:
        return "Empty"
    else:
        q.pop(0)
        
def peek(q):
    if isEmpty(q)==True:
        return "Item is not in the Queue"
    
    else:
        return q[0]
    
    
def Display(q):
    for i in range(len(q)):
        print(q[i],end=" ")
        
        


enqueue(Q, 44)
enqueue(Q, 65)
enqueue(Q, 21)

Display(Q)
print()
print(dequeue(Q))
print(peek(Q))
Display(Q)



