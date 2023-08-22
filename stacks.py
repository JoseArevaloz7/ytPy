class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)
     
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        last_element = self.stack[len(self.stack)-1]
        return last_element
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())