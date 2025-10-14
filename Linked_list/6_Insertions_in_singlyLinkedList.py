class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next  = self.head
        self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


 # desire position based insertion   
    def insert_at_position(self,data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next =  self.head
            self.head = new_node
            return
        current = self.head
        for i in range(position - 1):
            if current is None:
                raise IndexError("position out of bounds")
            current = current.next
        new_node.next = current.next
        current.next = new_node

# insertion after a given  node
    def insert_after_node(self,prev_node, data):
        if not prev_node:
            print("the given previous node must in linked list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node



# insertion before a given node
    def insert_before_node(self, next_node, data):
        if not next_node:
            print("the given next node must be in linked list")
            return
        new_node = Node(data)
        if self.head == next_node:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current and current.next != next_node:
            current =  current.next
        if current is None:
            print("the given next node is not present in linked list")
            return
        new_node.next = next_node
        current.next = new_node

# displaying the linked list    
    def display(self):
        current = self.head
        while current:
            print(current.data , end= " -> ")
            current = current.next
        print("None")



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
    sll.insert_at_position(25,2)
    sll.display()
    sll.insert_after_node(sll.head.next,27)
    sll.display()
    sll.insert_before_node(25,21)
    sll.display()