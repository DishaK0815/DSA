class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class CircularyDoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self,data):
        Newnode = Node(data)
        if self.head is None:
            self.head = Newnode
            Newnode.next = self.head
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = Newnode
        Newnode.prev = current
        Newnode.next = self.head
        self.head.prev = Newnode

    def forward_traversal(self):
        if self.head is None:
            print("Circular Doubly Linked List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
    
    def backward_traversal(self):
        if self.head is None:
            print("Circular Doubly Linked List is empty")
            return
        current = self.head.prev
        while True:
            print(current.data, end=" ")
            current = current.prev
            if current == self.head.prev:
                break
            
        
        
if __name__ == "__main__":
    cdl = CircularyDoublyLinkedList()
    cdl.insert_at_end(10)
    cdl.insert_at_end(20)
    cdl.insert_at_end(30)
    cdl.insert_at_end(40)
    cdl.insert_at_end(50)
    cdl.forward_traversal()
    print()
    cdl.backward_traversal()