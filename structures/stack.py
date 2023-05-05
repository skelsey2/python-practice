# Stack -  Data Structure

# Chat GPT's implementation of a Stack
# In this implementation, the Stack class has five methods:
# __init__: Initializes an empty list to store the stack elements.
# push: Adds an element to the top of the stack.
# pop: Removes and returns the element from the top of the stack. If the stack is empty, returns None.
# is_empty: Returns True if the stack is empty, False otherwise.
# peek: Returns the element at the top of the stack without removing it. If the stack is empty, returns None.
# size: Returns the number of elements in the stack.
class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
    def is_empty(self):
        return len(self.items) == 0
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def size(self):
        return len(self.items)
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())    # Output: 3
print(stack.pop())     # Output: 3
print(stack.pop())     # Output: 2
print(stack.is_empty())    # Output: False
print(stack.size())    # Output: 1


# does python have a built-in stack?
#   Yes, Python has a built-in stack implementation called `list`. In Python, a `list` can be used as a 
#       stack data structure by using the `append` method to add elements to the end of the list and the `pop` 
#       method to remove and return elements from the end of the list (which corresponds to the top of the 
#       stack).

# Here's an example of using a `list` as a stack in Python:
stack = []
stack.append(1)
stack.append(2)
stack.append(3)

print(stack[-1])    # Output: 3
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(len(stack) == 0)  # Output: False
print(len(stack))   # Output: 1

# In this example, we create an empty `list` and use the `append` method to add three elements to the end 
#   of the list, which simulates adding elements to the top of a stack. We then use the `-1` index to access 
#   the top element of the stack without removing it, and use the `pop` method to remove and print the top 
#   two elements (3 and 2). Finally, we use the `len` function to check whether the stack is empty and to 
#   print the current size of the stack.