# Reverse Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insertion(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        
    def reverse(self):
        temp = None
        current = self.head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            self.head = temp.prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == '__main__':
    llist = DoublyLinkedList()
    llist.insertion(2)
    llist.insertion(4)
    llist.insertion(8)
    llist.insertion(10)
    print("Original Linked List:")
    llist.display()
    llist.reverse()
    print("\nReversed Linked List:")
    llist.display()
 
