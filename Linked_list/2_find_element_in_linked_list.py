class Node:
    def __init__(self,data1,next1 = None):
        self.data = data1
        self.next = next1

def Find_element_in_list(head,desired_element):
    temp = head
    while temp is not None:
        if temp.data == desired_element:
            return True
        
        temp = temp.next
    return False

if __name__ == '__main__':
    arr = [1,4,6,7,78,3]
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])
    head.next.next.next.next = Node(arr[4])
    head.next.next.next.next.next = Node(arr[5])

    val = 78
    print(Find_element_in_list(head,val))