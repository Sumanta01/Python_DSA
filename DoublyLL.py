# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 18:58:04 2023

@author: KIIT
"""

class Node:
    def __init__(self,data):
        self.item=data
        self.next=None
        self.prev=None
        
class DoublyLinkedList:
    def __init__(self):
        self.start_node=None
        
    def InsertToEmpty(self,data):
        if self.start_node is None:
            new_node=Node(data)
            self.start_node=new_node
            
        else:
            print("The Linked List is Empty..")
    
    
    def InsertToEnd(self,data):
        if self.start_node is None:
            new_node=Node(data)
            self.start_node=new_node
            return
        
        n=self.start_node
        
        while n.next is not None:
            n=n.next
            new_node=Node(data)
            n.next=new_node
            new_node.prev=n
            
    def DeleteAtStrat(self):
        if self.start_node is None:
            print("The linked list is empty ..")
            return
        if self.start_node.next is None:
            self.start_node=None
            return
        
        self.start_node=self.start_node.next
        self.start_prev=None
        
    def DeleteAtEnd(self):
        if self.start_node is None:
            print("The linkedList is Empty")
            return
        if self.start_node.next is None:
            self.start_node=None
            return
        n=self.start_node
        while n.next is not None:
            n=n.next
            n.prev.next=None
            
    def Display(self):
        if self.start_node is None:
            print("The Linked List is empty...")
            return
        else:
            n=self.start_node
            while n is not None:
                print("The items are ",n.item)
                n.next
                
        print("\n")
        
    

NewDLL=DoublyLinkedList()
NewDLL.InsertToEmpty(10)
NewDLL.InsertToEnd(20)
NewDLL.InsertToEnd(30)
NewDLL.InsertToEnd(40)
NewDLL.InsertToEnd(50)
NewDLL.InsertToEnd(60)

NewDLL.Display()
    
                
            
        
            
    