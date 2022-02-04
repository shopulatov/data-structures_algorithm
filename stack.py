"""
Created on Tue Feb  1 08:47:47 2022

"""
class Stack:
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack[-1]

