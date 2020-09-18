#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:11:30 2020

@author: taylor
"""

# =============================================================================
# Class Node
# =============================================================================

###this was given to us in the assignment as a starting point
###this class definition creates the attributes value and next for class node
###and defines how to print out a node
class Node:
    def __init__(self, _value=None, _next=None):
        self.value = _value
        self.next = _next
    def __str__(self):
        return str(self.value)
    
# =============================================================================
# Class linkedList
# =============================================================================
    
###defining class linked list
class linkedList:
    def __init__(self, _value=None):
        #initializing with attributes head and count
        self.head= _value
        #starting count at one because the user will create list with node
        self.count = 1 
    
    #now I define a counter to keep track of how long the list is
    def length(self):
        return self.count
    
    #this defines how to print the list
    def __str__(self):
        #it will print this statement if there is nothing in the list
        if self.head == None:
            print("There is nothing in this list.")
        else:
            list = ""
            current = self.head
            #this while loop will go through each node in the list and print it
            while current.next != None:
                list += str(current.value) + ', '
                current = current.next
            list = list + str(current.value)
            return("This linked list is: " + list)
    
    #defining how to add a node to the end of the list 
    def addNode(self, new_value = None):
        #we are only accepting integers as nodes
        if type(new_value) == int:
            #create node of class Node
            new = Node(new_value)
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = new
            #update the counter
            self.count = self.count + 1
        else:
            print("New node values must be integers.")
            
    #defining how to add a node at specific point: after
    def addNodeAfter(self, new_value, after_node):
        #only accepting integers again
        if type(new_value) == int:
            #create node of class Node
            new = Node(_value = new_value)
            afternode = self.head
            #cannot use this if the list is empty
            if self.head == None:
                print("There are nodes in this list yet.")
            elif self.head.value == after_node.value:
                new.next = self.head.next
                self.head.next = new
            else:
                while(afternode.value != after_node.value):
                    afternode = afternode.next
                new.next = afternode.next
                afternode.next = new
            #add to counter
            self.count = self.count + 1
        else:
            print("New node values must be integers.")
                 
    #almost exactly the same as above
    def addNodeBefore(self, new_value, before_node):
        if type(new_value) == int:
            new = Node(_value = new_value)
            beforenode = self.head
            if self.head == None:
                print("There are no nodes in this list yet.")
            elif self.head.value == before_node.value:
                head = self.head
                self.head = new
                new.next = head
            else:
                while beforenode.value != before_node.value:
                    beforenode = beforenode.next
                new.next = beforenode.next
                beforenode.next = new
            self.count = self.count + 1
        else:
            print("New node values must be integers.")
    
    #defining how to remove a node
    def removeNode(self, node_to_remove):
        new = self.head
        #we are continually moving items through the list to head
        #in order to find the right node
        while new.next.value != node_to_remove.value:
            new = new.next
        new.next = node_to_remove.next
        #update counter
        self.count = self.count - 1
             
    #define removing from specific spot
    #this function is teeny but took me so long boo
    def removeNodesByValue(self, value):
        delete = self.head
        while delete.next.value != value:
            delete = delete.next
        delete.next = delete.next.next
        #update counter
        self.count = self.count - 1
    
    #finally, here is how to reverse list:
    def reverse(self):
        previous = None
        current = self.head
        while current != None:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
        self.head = previous
        
# =============================================================================
# Does it work?
# =============================================================================

#make an initial node
node1 = Node(1)

#make this node the head of the list
linkList = linkedList(node1)    

#length of list should be 1
linkList.length()

# adding two nodes
linkList.addNode(2)
linkList.addNode(3)

#length should be 3 now 
linkList.length()

#placing nodes in specific spots on the list
#also demonstrating print() function
linkList.addNodeAfter(4, Node(3))
linkList.addNodeAfter(5, Node(4))
print(linkList)

#removing node 5
linkList.removeNode(Node(5))
print(linkList)

#putting 0 in with the addNodeBefore function
linkList.addNodeBefore(0, Node(1))
print(linkList)

#removing 3 from list by value
linkList.removeNodesByValue(3)
print(linkList)

## this should reverse our list
linkList.reverse()
print(linkList)