class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            new_node.prev = current

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insert_after_node(self, target_data, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.data != target_data:
                current = current.next
                if current == self.head:
                    print(f"Node with data {target_data} not found.")
                    return
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
    
    def insert_before_node(self, target_data, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next.data != target_data:
                current = current.next
                if current.next == self.head:
                    print(f"Node with data {target_data} not found.")
                    return
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
    
    def insert_at_position(self, position, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
                if current == self.head:
                    print(f"Position {position} is out of range.")
                    return
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
    def display(self):
        if self.head is None:
            print("Circular Linked List is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()

if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.insert_at_end(10)
    cll.insert_at_end(20)
    cll.insert_at_end(30)
    cll.insert_at_beginning(5)
    cll.insert_after_node(20, 25)
    cll.insert_before_node(30, 28)
    cll.insert_at_position(2, 15)
    cll.display()

    
