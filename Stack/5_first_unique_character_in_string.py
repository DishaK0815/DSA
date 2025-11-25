class Solution(object):
    def firstUniqChar(self, s):
        
        char_count = {}
        stack = []

        #  Traverse and fill dictionary and stack
        for i, ch in enumerate(s):
            char_count[ch] = char_count.get(ch, 0) + 1
            stack.append((ch, i))

        #  Pop from stack until we find a unique character
        for ch, idx in stack:
            if char_count[ch] == 1:
                return idx

        return -1
