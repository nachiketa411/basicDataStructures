class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Push a new item onto the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item from the stack without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def __str__(self):
        """Return a string representation of the stack."""
        return str(self.items)


