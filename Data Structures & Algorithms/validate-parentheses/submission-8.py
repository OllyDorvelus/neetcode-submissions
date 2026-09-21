class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {'[': ']', '{': '}', '(': ')'}
        stack = []
        for char in s:
            if char in char_map.values():
                if len(stack) == 0 or char != char_map[stack.pop()]: 
                    return False
            else:
                stack.append(char)
        return len(stack) == 0