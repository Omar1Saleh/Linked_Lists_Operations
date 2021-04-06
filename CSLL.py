#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 20:00:34 2021

@author: oalhajj
"""
# creating nodes 
class Node:
    def __init__(self, value=None):
        self.value= value
        self.next= None
        
#operating on list        
class Circular_Singly_Linked_List:
    
    #initiating head and tail of  list 
    def __init__(self):
        self.head=None
        self.tail=None
        
    #making list iterable 
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node= node.next
            if node == self.tail.next: break
        
    #creating nodes to list 
    def list_creation(self, value):
        if self.head==None and self.tail==None:
            new_node=Node(value)
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
            print('The Csll list has been created!')
        print('The Csll list already exists!')
            
    #inserting to list 
    def list_insertion(self, value, location):
        new_node=Node(value)
        if self.head==None :
            print('This list doesn`t exist!')
        else:
            if location==0:
                new_node.next=self.head
                self.head=new_node
                self.tail.next=new_node
            elif location==-1:
                new_node.next=self.head
                self.tail.next=new_node
                self.tail=new_node
            else:
                temp_node=self.head
                index=0
                while index < location-1 :
                    temp_node=temp_node.next
                    index+=1
                next_node=temp_node.next
                temp_node.next=new_node
                new_node.next=next_node
                if temp_node == self.tail:
                    self.tail=new_node
                    self.tail.next=self.head
                    
    #taversing through singly linkedlist 
    def list_traversal(self):
        if self.head is None:
            print('This list doesn`t exist.')
        else:
            temp_node=self.head
            while temp_node:
                print(temp_node.value)
                temp_node=temp_node.next
                if temp_node==self.tail.next:
                    break
              
    #searching in SLL
    def list_search(self, nodeValue):
        if self.head is None:
            return "There is not any node in this CSLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The node does not exist in this CSLL"
                
            
    #deletion in list 
    def list_deletion(self, location):
        if self.head==None:
            print('This list doesn`t exist.')
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.tail.next=self.head
            elif location==-1:
                 if self.head==self.tail:
                     self.head=None
                     self.tail=None
                 else:
                     temp_node=self.head
                     while temp_node:
                         if temp_node.next==self.tail:
                             break
                         temp_node=temp_node.next
                     temp_node.next=self.head
                     self.tail=temp_node
            else:
                temp_node=self.head
                index=0
                while index < location-1:
                    temp_node=temp_node.next
                    index+=1
                next_node=temp_node.next
                temp_node.next=next_node.next
                if next_node==self.tail:
                    self.tail=temp_node
                    temp_node.next=self.head
    #delet entire list 
    def list_remove(self):
        if self.head==None:
            print('This list doesn`t exist.')
        else:
            self.head=None
            self.tail=None
#code ends here 
#testing 
csll=Circular_Singly_Linked_List()
csll.list_creation(1)
csll.list_insertion(0,0)
csll.list_insertion(2,2)
csll.list_insertion(3,-1)
csll.list_insertion(4,-1)
print([i.value for i in csll])
csll.list_traversal()
csll.list_deletion(-1)
csll.list_deletion(2)
csll.list_deletion(4)
csll.list_search(3)
csll.list_remove()
