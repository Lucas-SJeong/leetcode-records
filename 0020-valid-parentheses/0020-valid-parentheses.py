class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        return

    def peek(self):
        if self.is_empty():
            return
        else:
            return self.top.data
        
    def pop(self):
        if self.is_empty():
            return
        else:
            temp = self.top.data
            self.top = self.top.next
            return temp
            
    def __str__(self):
        ans = ""
        current = self.top
        while current:
            ans += str(current.data) + "\n"
            current = current.next

        return ans

class Solution(object):
    def isValid(self, s):
        top = ""
        brackets = {")":"(","}":"{","]":"["}
        stack = Stack()
        for element in s:
            if element in brackets.values():
                stack.push(element)
            else:
                if stack.peek()==brackets[element]:
                    stack.pop()
                else:
                    return False

        if stack.is_empty():                   
            return True  
        else:
            return False        
                
                