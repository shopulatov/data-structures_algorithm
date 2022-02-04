"""
Created on Mon Jan 31 19:49:23 2022

"""
class Node:
   def __init__(self, data):
       self.data = data
       self.next = None

class LinkedLists:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print('Node does not exist')
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def append(self, new_data):
        new_node = Node (new_data)
        
        if self.head is None:
            self.head = new_node
        
        last = self.head
        
        while last.next:
            last = last.next
        
        last.next = new_node
        
    def deleteNode(self, value):
        
        temp = self.head
        
        if (temp and temp.data == value):
            self.head = temp.next
            temp = None
        
        while temp:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
            
        if temp == None:
            return
        
        prev.next = temp.next
        temp = None