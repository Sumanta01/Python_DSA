# -*- coding: utf-8 -*-
"""
Created on Mon May 15 01:37:59 2023

@author: KIIT
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
        
        
class LinkedList:
    head=None
    def __int__(self):
        self.head=None
    
    def print_LL(self):
        if self.head is None:
            print("LInked List is empty")
            
        else:
            n=self.head
            while n is not None:
                print(n.data,end="-->")
                n=n.ref
                
    def add_begin(self,data):
       new_node=Node(data)
       new_node.ref=self.head
       self.head=new_node
       
       
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            
        else :
            n=self.head
            while n.ref is not None:
                n=n.ref
            
            n.ref=new_node
    
if __name__=="__main__":
    LL=LinkedList()
    LL.add_begin(76)
    LL.add_begin(65)
    LL.add_begin(123)
    LL.add_end(543)
    LL.add_end(22)
    LL.add_end(87)
    
    LL.print_LL()
 
        