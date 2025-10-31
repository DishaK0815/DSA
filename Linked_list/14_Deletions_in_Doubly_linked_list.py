class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
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
        NewNode.prev = current
        current.next = NewNode
    
    def Delete_from_end(self):
        if self.head is None:
            return
        current = self.head
        while current.next:
            current = current.next
        current.prev.next = None
        
    def Delete_from_begin(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.head.prev = None
    
    def Delete_after_node(self, node):
        if node is None or node.next is None:
            return
        node.next = node.next.next
        if node.next:
            node.next.prev = node
    def Delete_before_node(self, node):
        if node is None or node.prev is None:
            return
        node.prev = node.prev.prev
        if node.prev:
            node.prev.next = node
    
    def Delete_at_position(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current = self.head
        for _ in range(position):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        
     
     
     
       
        
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end = " <-> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    DLL = DoublyLinkedList()
    DLL.insertion(10)
    DLL.insertion(20)
    DLL.insertion(30)
    DLL.insertion(40)
    DLL.insertion(50)
    DLL.insertion(60)
    DLL.insertion(70)
    DLL.display()
    DLL.Delete_from_end()
    DLL.display()
    DLL.Delete_from_begin()
    DLL.display()
    DLL.Delete_after_node(DLL.head.next)
            
            
            
            
            
            
            
            
            
            
            