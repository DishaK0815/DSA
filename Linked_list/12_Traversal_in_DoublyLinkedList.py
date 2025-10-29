# Traversal in Doubly linked list
# forward traversal and backward traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertion(self,data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = NewNode
        NewNode.prev = current
    
    def forward_traversal(self):
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print("None")
    
    def backward_Traversal(self):
        current = self.head
        if current is None:
            return
        while current.next:
            current = current.next
        while current:
            print(current.data, end = " -> ")
            current = current.prev
        print("None")
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end = " <-> ")
            current = current.next
        print("None")
    



if  __name__ == "__main__":
    DLL = DoublyLinkedList()
    DLL.insertion(10)
    DLL.insertion(20)
    DLL.insertion(30)
    DLL.insertion(40)
    DLL.forward_traversal()
    DLL.backward_Traversal()
    DLL.display()
    
