# Sample simulations for stack
from Stack import Stack

def run_stack_simulations():
    stack = Stack()
    print("Is the stack empty?", stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack after pushing 1, 2, 3:", stack)
    print("Top item is:", stack.peek())
    print("Stack size is:", stack.size())
    print("Popped item:", stack.pop())
    print("Stack after popping:", stack)
    print("Is the stack empty?", stack.is_empty())

run_stack_simulations()