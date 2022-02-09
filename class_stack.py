class Stack:
    abc = 5
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        result = bool(self.stack)
        return result
    def push(self, index, element):
        self.stack.insert(index, element)
    def pop(self):
        self.stack.pop(0)
        if len(self.stack) == 0:
            return False
        else:
            return self.stack[0]
    def peek(self):
        return self.stack[0]
    def size(self):
        return len(self.stack)