class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = NewNode
        NewNode.prev = current

    def insert_at_beginning(self,data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            return
        else:
            NewNode.next = self.head
            self.head.prev = NewNode
            self.head = NewNode
    def insert_after_node(self, prev_node , data):
        if prev_node is None:
            print("Previous node is not in the list")
            return
        NewNode = Node(data)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next:
            NewNode.next.prev = NewNode
    
    def insert_before_node(self,after_node, data):
        if after_node is None:
            print("After node is not in the list")
            return
        NewNode = Node(data)
        NewNode.prev = after_node.prev
        NewNode.next = after_node
        after_node.prev = NewNode
        if NewNode.prev:
            NewNode.prev.next = NewNode
    
    def insert_at_posititon(self,data,position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        NewNode = Node(data)
        current = self.head
        for _ in range(position - 1):
            if current is None:
                print("Position out of range")
                return
            current = current.next
        if current is None:
            print("Position out of range")
            return
        NewNode.next = current.next
        current.next = NewNode
        NewNode.prev = current
        if NewNode.next:
            NewNode.next.prev = NewNode
        
        

    def display(self):
        current = self.head
        while current:
            print(current.data, end = " <-> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    DLL = DoublyLinkedList()
    DLL.insert_at_end(10)
    DLL.insert_at_end(20)
    DLL.insert_at_end(30)
    DLL.insert_at_end(40)
    DLL.insert_at_beginning(5)
   
    DLL.insert_after_node(DLL.head.next, 15)
    DLL.insert_before_node(DLL.head.next.next.next.next, 25)
    DLL.insert_at_posititon(35, 3)
    DLL.display()