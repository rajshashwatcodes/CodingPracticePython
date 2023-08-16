stack1 = []
stack2 = []

def enqueue(item):
    stack1.append(item)

def dequeue():
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
    if stack2:
        return stack2.pop()
    else:
        return None

# Test Code
enqueue(1)
enqueue(2)
enqueue(3)

print(dequeue())  
print(dequeue())  
print(dequeue())  
