class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def insert_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            
    def display(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return
        current = self.head
        while True:
            print(current.value, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("Head")

if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.insert_end(1)
    cll.insert_end(2)
    cll.insert_end(3)
    cll.insert_end(4)
    cll.insert_end(5)
    cll.insert_end(6)
    cll.display()