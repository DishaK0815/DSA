# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# optimal approach
class solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
# using recursion
class Solution(object):
    def deleteNode(self, node):
        if node.next.next  is None:
            node.val = node.next.val
            node.next = None
        else:
            node.val = node.next.val
            self.deleteNode(node.next)
#using  iteration
class Solution(object):
    def deleteNode(self, node):
        while node.next.next is not None:
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None
