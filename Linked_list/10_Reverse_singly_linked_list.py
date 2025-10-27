class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
class SinglyLinkedList:
    def  __init__(self):
        self.head = None
    
    def insertions(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode


    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        current = self.head
        while current :
                print(current.data, end = " -> ")
                current = current.next
        print("None")

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insertions(1)
    sll.insertions(2)
    sll.insertions(3)
    sll.insertions(4)
    sll.insertions(5)
    print("Original Linked List:")
    sll.display()
    sll.reverse()
    print("Reversed Linked List:")
    sll.display()
