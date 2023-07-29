# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 01:04:29 2023

@author: KIIT
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
        
        
# Create LinkedList
class LinkedList:
    def __init__(self):
        self.head=None
        
        
    def printL(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end=" ")
            print("-->",end=" ")
            temp=temp.next
            
            

Li=LinkedList()
first=Node(11)
second=Node(22)
third=Node(33)
        
Li.head=first
first.next=second
second.next=third

Li.printL()