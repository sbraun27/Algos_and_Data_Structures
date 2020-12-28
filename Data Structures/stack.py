# LIFO: Last item we insert, is the first item we take out
class Stack():
    def __init__(self):
        self.stack = []

    # insert item into the stack // O(1)
    def push(self, data):
        self.stack.append(data)

    # remove and return the last item we have inserted // O(1)
    def pop(self):

        if self.stack_size() < 1:
            return

        data = self.stack[-1]
        del self.stack[-1]
        return data

    # peek: returns the last item without removing it // O(1)
    def peek(self):
        if self.stack_size() < 1:
            return
        return self.stack[-1]

    # has O(1) running time
    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Size of stack is: {stack.stack_size()}")
    print(f"Popped item is: {stack.pop()}")
    print(f"Size of stack is: {stack.stack_size()}")
    print(f"Popped item is: {stack.pop()}")
    print(f"Size of stack is: {stack.stack_size()}")
    print(f"Popped item is: {stack.pop()}")
    print(f"Size of stack is: {stack.stack_size()}")
    print(f"Popped item is: {stack.pop()}")
    print(stack.peek())
