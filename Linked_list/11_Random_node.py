import random
class Solution(object):

    def __init__(self, head):
        self.nodes = []
        while head:
            self.nodes.append(head.val)
            head = head.next
        
        

    def getRandom(self):
        return random.choice(self.nodes)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
class Solution2(object):

    def __init__(self, head):
        self.head = head
        

    def getRandom(self):
        result, node, index = None, self.head, 0
        while node:
            if random.randint(0, index) == 0:
                result = node.val
            node = node.next
            index += 1
        return result

class Solution3(object):

    def __init__(self, head):
        self.head = head
        

    def getRandom(self):
        result, node, index = None, self.head, 1
        while node:
            if random.random() < 1.0 / index:
                result = node.val
            node = node.next
            index += 1
        return result