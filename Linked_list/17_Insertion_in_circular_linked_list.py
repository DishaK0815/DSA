# insertions in circular singly linked list
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            NewNode.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = NewNode
        NewNode.next = self.head

    def insert_at_begin(self,data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            NewNode.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = NewNode
        NewNode.next = self.head
        self.head = NewNode

        

    

    def insert_after_node(self, data, prev_node):
        NewNode = Node(data)
        current = self.head
        while current.data != prev_node:
            current = current.next
        
        NewNode.next = current.next
        current.next = NewNode

    def insert_before_node(self,data, after_node):
        NewNode = Node(data)
        current = self.head
        while current.next.data != after_node:
            current = current.next
        NewNode.next = current.next
        current.next = NewNode
   
    def insert_at_index(self,data,position):
        NewNode = Node(data)
        current = self.head
        if position == 0:
            NewNode.next = self.head
            self.head = NewNode

        for i in range(position - 1):
            current = current.next
        
        NewNode.next = current.next
        current.next = NewNode


    def display(self):
        if self.head is None:
            print("Circular Linked List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("Head")

if __name__ == "__main__":
    cll = CircularSinglyLinkedList()
    cll.insert_at_end(10)
    cll.insert_at_end(20)
    cll.insert_at_end(30)
    cll.insert_at_end(40)
    cll.insert_at_end(50)
    cll.insert_at_end(60)
    cll.display()
    cll.insert_at_begin(5)
    cll.display()
    cll.insert_after_node(70, 60)
    cll.display()
    cll.insert_before_node(65, 70)
    cll.display()
    # cll.insert_at_index(9, 0)
    # cll.display()
