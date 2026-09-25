class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close_dict = {'[': ']', '{': '}', '(': ')'}
        stack = []
        for char in s:
            if char in open_to_close_dict.keys():
                stack.append(char)
                continue
            if len(stack) == 0 or open_to_close_dict[stack.pop()] != char:
                return False
        return not len(stack)