class Node:
    def __init__(self,data1,next1= None):
        self.data = data1
        self.next = next1

def Length_of_LinkedList(head):
    count = 0
    temp = head

    while temp is not None:
        temp = temp.next
        count += 1
    return count
def main():
    nums = [2,5,9,5,3]
    head = Node(nums[0])
    head.next = Node(nums[1])
    head.next.next = Node(nums[2])
    head.next.next.next = Node(nums[3])
    head.next.next.next.next = Node(nums[4])
    print("length of linked list:", Length_of_LinkedList(head))
main()

