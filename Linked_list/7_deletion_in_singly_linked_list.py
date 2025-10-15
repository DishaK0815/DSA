class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(position - 1):
            if current is None:
                raise IndexError("Position out of bounds")
            current = current.next
        new_node.next = current.next
        current.next = new_node
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("The given previous node must be in linked list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def insert_before_node(self, next_node_data, data):
        new_node = Node(data)
        if self.head and self.head.data == next_node_data:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current and current.next and current.next.data != next_node_data:
            current = current.next
        if current is None or current.next is None:
            print("The given next node is not present in linked list")
            return
        new_node.next = current.next
        current.next = new_node

    # Deletion methods
    def delete_from_beginning(self):
        if self.head:
            self.head = self.head.next

    def delete_from_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
    def delete_by_value(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        if current.next:
            current.next = current.next.next

    def delete_at_position(self, position):
        if position == 0 and self.head:
            self.head = self.head.next
            return
        current = self.head
        for i in range(position - 1):
            if not current or not current.next:
                raise IndexError("Position out of bounds")
            current = current.next
        if current.next:
            current.next = current.next.next

    def delete_after_node(self, prev_node_data):
        current = self.head
        while current and current.data != prev_node_data:
            current = current.next
        if current and current.next:
            current.next = current.next.next

    def delete_before_node(self, next_node_data):
        if not self.head or self.head.data == next_node_data:
            return
        if self.head.next and self.head.next.data == next_node_data:
            self.head = self.head.next
            return
        prev = None
        current = self.head
        while current.next and current.next.data != next_node_data:
            prev = current
            current = current.next
        if prev and current.next:
            prev.next = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_beginning(10)
    sll.insert_at_beginning(20)
    sll.insert_at_beginning(30)
    sll.insert_at_beginning(40)
    sll.display()

    sll.insert_at_end(50)
    sll.insert_at_end(60)
    sll.display()

    sll.insert_at_position(25, 2)
    sll.display()

    sll.insert_after_node(sll.head.next, 27)
    sll.display()

    sll.insert_before_node(25, 21)
    sll.display()

    sll.delete_from_beginning()
    sll.display()

    sll.delete_from_end()
    sll.display()

    sll.delete_by_value(27)
    sll.display()

    sll.delete_at_position(2)
    sll.display()

    sll.delete_after_node(21)
    sll.display()

    sll.delete_before_node(25)
    sll.display()