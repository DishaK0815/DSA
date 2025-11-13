# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head           
        
class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next.val else head
    
class Solution:
    def deleteDuplicates(self, head):
        prev = head
        curr = head.next if head else None
        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head