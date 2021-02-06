class Stack():
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items
my_stack = Stack()
my_stack.push('Shakeel')
my_stack.push('Majeed')
my_stack.push(2021)
print(my_stack.get_stack())
print(my_stack.peek())
