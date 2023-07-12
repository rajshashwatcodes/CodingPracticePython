class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)


# Example usage
stack = Stack()
print("Is stack empty?", stack.is_empty())  # True

stack.push(1)
stack.push(2)
stack.push(3)
print("Stack size:", stack.size())  # 3
print("Top item in stack:", stack.peek())  # 3

popped_item = stack.pop()
print("Popped item:", popped_item)  # 3
print("Stack size:", stack.size())  # 2
