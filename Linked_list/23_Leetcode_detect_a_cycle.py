# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        # Using a Hash Set
        visited = set()
        current = head
        while current:
                if current in visited:
                    return current
                visited.add(current)
                current = current.next
        return None

        
        # floydd's Cycle detection
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        else: return None
        while head != slow:
            head, slow = head.next , slow.next
        return head
        
        