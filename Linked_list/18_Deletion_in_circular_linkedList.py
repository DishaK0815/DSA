# Deletion in Circular Linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            NewNode.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = NewNode
            NewNode.next = self.head

    def delete_at_end(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        while current.next.next != self.head:
            current = current.next
        current.next = self.head
    
    def delete_at_begin(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return
        if self.head.next == self.head:
            self.head = None
    
    def delete_after_node(self, after_node):
        if self.head is None:
            print("Circular Linked List is empty")
            return
        current = self.head
        while current.data != after_node:
            current = current.next
        current.next = current.next.next
    
    def delete_before_node(self, before_node):
        if self.head is None:
            print("Circular Linked List is empty")
            return
        if self.head.next.data == before_node:
            self.head = self.head.next
            return
        current = self.head
        while current.next.next.data != before_node:
            current = current.next
        current.next = current.next.next

    def delete_at_position(self, position):
        if self.head is None:
            print("Circular Linked List is empty")
            return
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(position - 1):
            current = current.next
        current.next = current.next.next

if __name__ == "__main__":
    CLL=CircularSinglyLinkedList()
    CLL.insert_at_end(10)
    CLL.insert_at_end(20)
    CLL.insert_at_end(30)
    CLL.insert_at_end(40)
    CLL.insert_at_end(50)   
    CLL.insert_at_end(60)
    CLL.delete_at_end()

    CLL.delete_at_begin()
    CLL.delete_after_node(30)
    CLL.delete_before_node(40)
    CLL.delete_at_position(1)


