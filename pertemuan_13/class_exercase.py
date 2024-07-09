class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pops(self):
        self.stack.pop()
        
    def peek(self):
        return self.stack[-1]
    
    def isMT(self):
        return True if len(self.stack) == 0 else False
    
    def print(self):
        print(self.stack)