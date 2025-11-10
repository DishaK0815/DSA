# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast = slow = head

        # Move fast pointer n steps ahead
        for i in range(n):
            fast = fast.next

        # If fast is None, we are removing the head
        # if they have exactly  same node then node to be remove is  head node
        if not fast:
            return head.next

        # Move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from end
        slow.next = slow.next.next

        return head

# Helper function to convert array to linked list
def array_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to array
def linked_list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example usage
if __name__ == "__main__":
    input_list = [1,2,3,4,5]
    n = 3
    head = array_to_linked_list(input_list)
    solution = Solution()
    new_head = solution.removeNthFromEnd(head, n)
    output_list = linked_list_to_array(new_head)
    print("Output:", output_list)  # Output: [1, 2, 3, 5]