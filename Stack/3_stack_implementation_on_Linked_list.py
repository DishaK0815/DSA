# stack implemetation on  Linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedListStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

if __name__ == "__main__":
    stack = LinkedListStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.pop())  # Output: 30
    print(stack.peek()) # Output: 20
    print(stack.is_empty()) # Output: False