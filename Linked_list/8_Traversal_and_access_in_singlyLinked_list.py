class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push_back(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # 1. Iterative Traversal
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    # 2. Recursive Traversal
    def traverse_recursive(self, node):
        if not node:
            return
        print(node.data, end=" ")
        self.traverse_recursive(node.next)

    def start_recursive_traversal(self):
        self.traverse_recursive(self.head)
        print()

    # 3. Reverse Traversal (Recursive)
    def reverse_print(self, node):
        if not node:
            return
        self.reverse_print(node.next)
        print(node.data, end=" ")

    def start_reverse_print(self):
        self.reverse_print(self.head)
        print()

    # 4. Access nth Node
    def get_nth(self, n):
        temp = self.head
        count = 0
        while temp:
            if count == n:
                return temp.data
            count += 1
            temp = temp.next
        return -1  # Out of bounds

    # 5. Length of List
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    # 6. Middle Node
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else -1

    # 7. Last Node
    def get_last(self):
        if not self.head:
            return -1
        temp = self.head
        while temp.next:
            temp = temp.next
        return temp.data

    # 8. kth Node from End
    def get_kth_from_end(self, k):
        first = self.head
        second = self.head
        for _ in range(k):
            if not first:
                return -1
            first = first.next
        while first:
            first = first.next
            second = second.next
        return second.data if second else -1


if __name__ == "__main__":
    sll = SinglyLinkedList()
    for i in range(1, 11):
        sll.push_back(i)
    print("Iterative Traversal:")
    sll.traverse()
    print("Recursive Traversal:")
    sll.start_recursive_traversal()
    print("Reverse Traversal:")
    sll.start_reverse_print()
    print("3rd Node:", sll.get_nth(3))
    print("Length of List:", sll.length())
    print("Middle Node:", sll.find_middle())
    print("Last Node:", sll.get_last())
    print("3rd Node from End:", sll.get_kth_from_end(3))
    for i in range(1, 12):
        sll.push_back(i)
    
