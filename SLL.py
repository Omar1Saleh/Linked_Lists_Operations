#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 20:41:44 2021

@author: oalhajj
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 08:14:17 2021

@author: oalhajj
"""
# creating nodes 
class Node:
    def __init__(self, value=None):
        self.value= value
        self.next= None
#operating on list        
class SinglyLinkedList:
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
    #inserting nodes to list 
    def list_insertion(self, value, location):
        new_node=Node(value)
        if self.head==None :
            self.head=new_node
            self.tail=new_node
        else:
            if location==0:
                new_node.next=self.head
                self.head=new_node
            elif location==-1:
                new_node.next=None
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
                    
    #taversing through singly linkedlist 
    def list_traversal(self):
        if self.head==None:
            print('This list doesn`t exist.')
        else:
            temp_node=self.head
            while temp_node is not None:
                print(temp_node.value)
                temp_node=temp_node.next
    #searching in SLL
    def list_search(self, value):
        if self.head==None:
            print('This list doesn`t exist.')
        else:
            temp_node=self.head
            while temp_node is not None:
                if temp_node.value==value:
                    return temp_node.value
                temp_node=temp_node.next
            return 'The Value Doesn`t exist.'
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
            elif location==-1:
                 if self.head==self.tail:
                     self.head=None
                     self.tail=None
                 else:
                     temp_node=self.head
                     while temp_node is not None:
                         if temp_node.next==self.tail:
                             break
                         temp_node=temp_node.next
                     temp_node.next=None
                     self.tail=temp_node
            else:
                temp_node=self.head
                index=0
                while index < location-1:
                    temp_node=temp_node.next
                    index+=1
                next_node=temp_node.next
                temp_node.next=next_node.next
                if next_node == self.tail:
                    self.tail=temp_node
                    
    #delet entire list 
    def list_remove(self):
        if self.head==None:
            print('This list doesn`t exist.')
        else:
            self.head=None
            self.tail=None
#code ends here 
#testing 
sll=SinglyLinkedList()
sll.list_insertion(1,5)
sll.list_insertion(1,1)
sll.list_insertion(2,2)
sll.list_insertion(3,-1)
print([i.value for i in sll])
sll.list_deletion(3)
sll.list_traversal()
sll.list_search(3)
sll.list_insertion(3, -1)
sll.list_deletion(1)
#heklp
