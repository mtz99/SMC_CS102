# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
#stack.py

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        temp = Stack()
        stringy = ""
        while not self.isEmpty():
            a = self.pop()
            temp.push(a)
            stringy = str(a) + stringy
        while not temp.isEmpty():
            self.push(temp.pop())
        return "["+stringy+")"        
        
