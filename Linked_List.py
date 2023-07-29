# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 18:57:26 2023

@author: KIIT
"""

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
    
class Linked_list:
    def __init__(self):
        self.head=None
        
    def insertAtBegin(self ,data):
        node=Node(data,self.head)
        self.head=node
        
        
    def Print(self):
        if self.head is None:
            print("Linked list is empty")
            return 
        
        itr=self.head
        l_str=''
        while(itr):
            l_str+=str(itr.data)+'-->'
            itr=itr.next
            
        print(l_str)
        
        
        
    def insertAtEnd(self ,data):
        if self.head is None:
            self.head=Node(data, None)
            return
        
        
        itr=self.head
        while itr.next:
           itr=itr.next
            
            
        itr.next=Node(data,None) 
    
    
    def insertValues(self ,data_list):
        self.head=None
        for data in data_list:
            self.insertAtEnd(data)
            
            
        
        
    def lengthOfLL(self):
        count=0;
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
            
        return count
    
    
    
    def remove_at(self ,index):
        if index<0 or index>self.lengthOfLL():
            raise Exception("Invalid Linkedlist")
            
            
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
        
    
        
if __name__=='__main__':
    
    ll=Linked_list()
    ll.insertAtBegin(76)
    ll.insertAtBegin(34)
    ll.insertAtBegin(65)
    ll.insertAtEnd(70)
    ll.insertAtEnd(1)
    ll.insertValues(["mango","audi","python","Bitcoin"])
    ll.lengthOfLL()
    ll.remove_at(2)
    ll.remove_at(0)
    ll.Print()
   

    
    
        

        
        
        
        
        