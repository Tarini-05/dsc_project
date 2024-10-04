class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
            return None
        return self.stack.pop()
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
            return None
        return self.stack[-1]

# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Top element is", s.peek()) 
print("Popped element is", s.pop()) 
print("Top element after pop is", s.peek())  
