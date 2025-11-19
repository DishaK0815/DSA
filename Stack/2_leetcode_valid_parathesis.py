class Solution(object):
    def isValid(self, s):
        
        stack = []
        # Mapping of closing to opening brackets
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():  # If it's an opening bracket
                stack.append(char)
            elif char in mapping:  # If it's a closing bracket
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False  # Invalid character (not needed here as per constraints)
        
        return not stack  # True if stack is empty

            